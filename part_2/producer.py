import pika

QUEUE_NAME = "persist_queue"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True)

if __name__ == '__main__':

    for i in range(5):
        message = f'{i}: hello'

        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )

        print(f"Отправили {message}")
