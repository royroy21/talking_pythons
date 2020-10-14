#!/usr/bin/env python
import logging
import sys

from app.connect import connect

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def main():
    connection, channel = connect()

    def callback(ch, method, properties, body):
        logger.info(' [x] Received %s', body)

    channel.basic_consume(
        queue='hello',
        on_message_callback=callback,
        auto_ack=True,
    )

    logger.info(' [x] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
