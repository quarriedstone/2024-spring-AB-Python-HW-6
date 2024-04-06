import time

import pika

QUEUE_NAME = "persist_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True)


def callback(ch, method, properties, body):
    time.sleep(2)
    print(f"Обработали {body}, delivery_tag={method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback,
    )

    print("Читаем сообщения")
    channel.start_consuming()
