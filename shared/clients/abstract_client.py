from abc import ABC, abstractmethod
from typing import Dict, Any


class AbstractClient(ABC):
    # pylint:disable=duplicate-code
    def __init__(self, **kwargs: Any) -> None:  # type: ignore
        self.session = self._create_session(**kwargs)

    @abstractmethod
    def _create_session(self, **kwargs: Any) -> Any:  # type: ignore
        pass

    @property
    @abstractmethod
    def headers(self) -> Dict[str, str]:
        pass

    @property
    @abstractmethod
    def cookies(self) -> Dict[str, str]:
        pass

    @headers.setter  # type: ignore
    @abstractmethod
    def headers(self, headers: Dict[str, str]) -> None:
        pass

    @cookies.setter  # type: ignore
    @abstractmethod
    def cookies(self, cookies: Dict[str, str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @property
    @abstractmethod
    def user_agent(self) -> str:
        pass
