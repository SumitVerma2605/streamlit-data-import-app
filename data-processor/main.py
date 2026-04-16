import logging
from celery import Celery
from app.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)

# Initialize Celery
celery_app = Celery(
    'data_processor',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.REDIS_URL
)

logger.info("🚀 Data Processor Celery Worker Started")

if __name__ == '__main__':
    celery_app.start()