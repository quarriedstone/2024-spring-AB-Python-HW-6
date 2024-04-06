import pika

from part_4.rabbit_types import MessageType

EXCHANGE_NAME = "message_exchange_direct"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME,
                         exchange_type='direct')

if __name__ == '__main__':

    for i in range(6):
        message = f'{i}: hello'
        routing_key = str(MessageType.green)

        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=routing_key,
            body=message,
        )

        print(f"Отправили {message}, {routing_key=}")
