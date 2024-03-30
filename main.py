from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.app import new_app
from app.settings import AppSettings

from health.repositories.health import HealthRepository
from health.services.health import HealthService
from ofertas.repositories.ofertas import OfertasRepository
from ofertas.services.ofertas import OfertasService

app_settings = AppSettings()
engine = create_async_engine(app_settings.database.dsn, pool_size=app_settings.database.pool_size)
session_maker = async_sessionmaker(bind=engine)

health_repository = HealthRepository(session_maker)
health_service = HealthService(health_repository)

ofertas_repository = OfertasRepository(session_maker)
ofertas_service = OfertasService(ofertas_repository)
cors_origin_whitelist = app_settings.cors_origin.whitelist

app = new_app(health_service,
              ofertas_service,
              cors_origin_whitelist.split(','))

