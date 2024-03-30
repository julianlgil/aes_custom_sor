from pydantic import BaseSettings, PostgresDsn



class DatabaseSettings(BaseSettings):
    dsn: PostgresDsn
    pool_size: int


class TelemetrySettings(BaseSettings):
    otel_collector_endpoint: str


class CorsSettings(BaseSettings):
    whitelist: str


class AppSettings(BaseSettings):
    app_name: str
    database: DatabaseSettings
    telemetry: TelemetrySettings
    cors_origin: CorsSettings

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'
