import pika

QUEUE_NAME = "start"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME)

if __name__ == '__main__':
    message = b'hello'

    for _ in range(5):
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=message,
        )

        print(f"Отправили {message}")
