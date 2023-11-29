import time
import pika
from urllib.parse import urlparse

# def init_connection():
#     # RabbitMQ connection URI
#     rabbitmq_uri = "amqp://guest:guest@localhost:5672"

#     # Parse the URI
#     uri_parts = urlparse(rabbitmq_uri)

#     # Construct connection parameters
#     credentials = pika.PlainCredentials(uri_parts.username, uri_parts.password)
#     parameters = pika.ConnectionParameters(
#         host=uri_parts.hostname,
#         port=uri_parts.port,
#         virtual_host=uri_parts.path[1:],  # Extract virtual host from path
#         credentials=credentials
#     )
#     return parameters


def send_message(message, routing_key):
    # connection_params = init_connection()
    # connection_params = pika.ConnectionParameters('localhost')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # connection = pika.BlockingConnection(connection_params)
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
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
while(True):    
    i += 1
    msg = "Hello World!" + str(i)
    send_message(msg, "info.messages")
    print(msg)
    time.sleep(1)
# send_message("Important message", "warning.alerts")
