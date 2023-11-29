import json
import time
import pika
from urllib.parse import urlparse
from Models.Address import AddressData, AddressDataEncoder
from Models.Person import Person


def init_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    return channel


def send_message_(channel, message, exchange, routing_key):
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost'))
    # channel = connection.channel()
    exchange_name = exchange
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(
            content_type='text/plain',
            delivery_mode=2,  # make the message persistent
        )
    )

    print(f" [x] Sent '{message}' with routing key '{routing_key}'")

    # connection.close()


def send_message(message, routing_key):
    # connection_params = init_connection()
    # connection_params = pika.ConnectionParameters('localhost')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # connection = pika.BlockingConnection(connection_params)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    exchange_name = 'python_producer'
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(
            content_type='text/plain',
            delivery_mode=2,  # make the message persistent
        )
    )

    print(f" [x] Sent '{message}' with routing key '{routing_key}'")

    connection.close()


# Example usage
i = 0
# while(True):
routing = "info.messages"
address = AddressData("Israel", "Haifa", "Hemda", 10)
kfir = Person("kfir abbou", 40, address)
kfirMsgBody = json.dumps(kfir.__dict__, cls=AddressDataEncoder)


send_message(kfirMsgBody, routing)

#     i += 1
#     msg = "Hello World!" + str(i)
#     send_message(msg, )
#     print(msg)
#     time.sleep(1)
# send_message("Important message", "warning.alerts")
