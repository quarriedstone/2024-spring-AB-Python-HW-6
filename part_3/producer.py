import pika

EXCHANGE_NAME = "message_exchange"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME,
                         exchange_type='fanout')

if __name__ == '__main__':

    for i in range(6):
        message = f'{i}: hello'

        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key='',
            body=message,
        )

        print(f"Отправили {message}")
