from celery import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name='add')
def add(x, y):
    logger.info("Sent ADD")
    return x + y


@task(name='mul')
def mul(x, y):
    logger.info("Sent MUL")
    return x * y


@task(name='xsum')
def xsum(numbers):
    logger.info("Sent XSUM")
    return sum(numbers)