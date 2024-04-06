import time

import pika

EXCHANGE_NAME = "message_exchange"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME,
                         exchange_type='fanout')

queue_result = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange=EXCHANGE_NAME,
                   queue=queue_result.method.queue)


def callback(ch, method, properties, body):
    time.sleep(2)
    print(f"Обработали {body}, delivery_tag={method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=queue_result.method.queue,
        on_message_callback=callback,
    )

    print(f"Читаем сообщения из очереди {queue_result.method.queue}")
    channel.start_consuming()
