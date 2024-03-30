import base64
import json
import logging
from typing import Optional

from fastapi import Header

from shared.errors import ResponseException, UNAUTHORIZED_ERROR

logger = logging.getLogger(__name__)


class PermissionChecker:

    def __init__(self, allowed_roles: set[str]) -> None:
        self.allowed_roles = allowed_roles

    # pylint: disable=too-many-arguments
    def _validate_roles(self,
                        id_to_validate: str,
                        roles: str,
                        is_tenant: bool,
                        auth_user_id: str,
                        auth_tenant_id: str,
                        auth_company_id: Optional[str] = None) -> bool:
        raw_roles = base64.b64decode(roles.encode('ascii')).decode('utf-8')
        roles_by_company = json.loads(raw_roles)
        company_roles = roles_by_company.get(id_to_validate, {}).get('roles', [])
        for role in company_roles:
            if role in self.allowed_roles:
                return True
        if is_tenant:
            logger.warning(
                'user %s (tenant: %s) does not have any of the expected roles %s',
                auth_user_id, auth_tenant_id, self.allowed_roles,
            )
        else:
            logger.warning(
                'user %s (tenant: %s, company: %s) does not have any of the expected roles %s',
                auth_user_id, auth_tenant_id, auth_company_id, self.allowed_roles,
            )
        raise ResponseException(UNAUTHORIZED_ERROR)


class PermissionCompanyChecker(PermissionChecker):
    def __call__(self,  # pylint: disable=too-many-arguments
                 company_id: str,
                 auth_user_id: str = Header(),
                 auth_tenant_id: str = Header(),
                 auth_company_id: str = Header(),
                 auth_companies_roles: str = Header()) -> bool:
        if company_id != auth_company_id:
            logger.warning('user %s (%s) does not belong to the expected company %s',
                           auth_user_id, auth_company_id, company_id)
            raise ResponseException(UNAUTHORIZED_ERROR)
        return self._validate_roles(id_to_validate=company_id,
                                    roles=auth_companies_roles,
                                    is_tenant=False,
                                    auth_user_id=auth_user_id,
                                    auth_tenant_id=auth_tenant_id,
                                    auth_company_id=auth_company_id)


class PermissionTenantChecker(PermissionChecker):
    def __call__(self,
                 tenant_id: str,
                 auth_user_id: str = Header(),
                 auth_tenant_id: str = Header(),
                 auth_tenants_roles: str = Header()
                 ) -> bool:
        if tenant_id != auth_tenant_id:
            logger.warning('user %s (%s) does not belong to the expected tenant %s',
                           auth_user_id, auth_tenant_id, tenant_id)
            raise ResponseException(UNAUTHORIZED_ERROR)
        return self._validate_roles(id_to_validate=tenant_id,
                                    roles=auth_tenants_roles,
                                    is_tenant=True,
                                    auth_user_id=auth_user_id,
                                    auth_tenant_id=auth_tenant_id)
