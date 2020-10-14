#!/usr/bin/env python
import logging
import sys
import time

from app.connect import connect

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def main():
    connection, channel = connect()

    for n in range(100):
        time.sleep(5)
        body = f'Hello {n}'
        logger.info(' [x] Sending %s', body)
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=body,
        )

    connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
