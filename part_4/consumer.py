import sys
import time

import pika

from part_4.rabbit_types import MessageType

EXCHANGE_NAME = "message_exchange_direct"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME,
                         exchange_type='direct')

queue_result = channel.queue_declare(queue='', exclusive=True)


def callback(ch, method, properties, body):
    time.sleep(2)
    print(f"Обработали {body}, delivery_tag={method.delivery_tag}, routing_key={method.routing_key}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':

    type_strings = sys.argv[1:]

    if type_strings:
        for type_str in type_strings:
            channel.queue_bind(exchange=EXCHANGE_NAME,
                               queue=queue_result.method.queue,
                               routing_key=str(MessageType(type_str)))
    else:
        channel.queue_bind(exchange=EXCHANGE_NAME,
                           queue=queue_result.method.queue,
                           routing_key='')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=queue_result.method.queue,
        on_message_callback=callback,
    )

    print(f"Читаем сообщения из очереди {queue_result.method.queue} c routing_keys={type_strings}")
    channel.start_consuming()
