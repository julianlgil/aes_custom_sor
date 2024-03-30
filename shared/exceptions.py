class CustomHTTPError(Exception):
    """Exception for handle HTTP errors
    from  differents request adapters types"""

    def __init__(self, status_code: int, message: str, original_url: str):
        self.status_code = status_code
        self.message = message
        self.original_url = original_url

    def __str__(self) -> str:
        return f'{self.status_code}: {self.message} for url: {self.original_url}'


class CustomTimeoutError(Exception):
    """Exception for handle timeout errors
    from differents request adapters types"""

    def __init__(self, url: str, method: str):
        self.url = url
        self.method = method

    def __str__(self) -> str:
        return f'TimeoutError calling: {self.method} {self.url}'
