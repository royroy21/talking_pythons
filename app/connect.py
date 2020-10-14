import logging
import os
import sys

import pika

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

RABBIT_QUEUE = 'hello'
CLOUDAMQP_URL = os.environ.get(
    'CLOUDAMQP_URL',
    'amqp://guest:guest@localhost:5672/%2f',
)


def connect():
    logger.info(' [x] Trying to connect to %s', CLOUDAMQP_URL)
    parameters = pika.URLParameters(CLOUDAMQP_URL)
    connection = pika.BlockingConnection(parameters)
    logger.info(' [x] Connection established')
    channel = connection.channel()
    channel.queue_declare(queue=RABBIT_QUEUE)
    logger.info(' [x] Using queue %s', RABBIT_QUEUE)
    return connection, channel
