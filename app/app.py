from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from health.services.health import HealthService
from health.views.health import register_health_view
from ofertas.services.ofertas import OfertasService
from ofertas.views.ofertas import register_ofertas_view
from shared.errors import register_error_handlers


def new_app(
    # pylint: disable=too-many-arguments
    # Six is reasonable in this case.
        health_service: HealthService,
        oferta_service: OfertasService,
        cors_origin_whitelist: List[str]
) -> FastAPI:
    app = FastAPI(title='Opt-In',
                  description='Credentials management microservice',
                  openapi_url='/cred-optin/v1/api/openapi.json',
                  servers=[{'url': '/'}, {'url': '/cred-optin/v1/api/'}]
                  )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origin_whitelist,
        allow_credentials=True,
        allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD'],
        allow_headers=['*'],
    )

    register_error_handlers(app)
    register_health_view(app, health_service)
    register_ofertas_view(app, oferta_service)
    return app
