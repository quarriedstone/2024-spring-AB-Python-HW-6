import pika

QUEUE_NAME = "start"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME)


def callback(ch, method, properties, body):
    print(f"Получил {body}")


if __name__ == '__main__':
    channel.basic_consume(
        queue=QUEUE_NAME,
        auto_ack=True,
        on_message_callback=callback,
    )

    print("Читая сообщения")
    channel.start_consuming()
