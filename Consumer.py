import pika
import json

from Models.CatheterPosition import CatheterPosition, CatheterPositionEncoder
from Producer import send_message_
position = CatheterPosition(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)


def callback(ch, method, properties, body):
    # print(f" [x] Received {body} with routing key '{method.routing_key}'")
    message = json.loads(body)

    if 'CommandType' in message:
        cmd = message['CommandType']
        if cmd == 0:  # Move Catheter
            # print('Move catheter command received...')
            position.move_catheter()

        elif cmd == 1:  # Get Position
            # print('Get position request')
            positionJson = json.dumps(
                position.__dict__, cls=CatheterPositionEncoder)
            send_message_(ch, positionJson, 'reply', 'CatheterPosition')
        elif cmd == 2:  # RESET_CATHETER_POSITION
            position.reset_position()
            pass
        elif cmd == 3:  # STOP_MOVE_CATHETER
            pass

    # elif :


def receive_messages(channels_data, channel):
    connection_params = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_params)

    channel = connection.channel()
    # exchange_name = 'pythonConsumer'

    for channel_data in channels_data:
        exchange_name = channel_data[1]
        binding_key = channel_data[0]

        channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=exchange_name,
                           queue=queue_name, routing_key=binding_key)

        print(
            f" [*] Waiting for messages with routing key '{binding_key}'. To exit press CTRL+C")

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


# def receive_messages(binding_key, exchange_name="pythonConsumer"):
#     connection_params = pika.ConnectionParameters('localhost')
#     connection = pika.BlockingConnection(connection_params)

#     channel = connection.channel()
#     # exchange_name = 'pythonConsumer'

#     channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

#     result = channel.queue_declare(queue='', exclusive=True)
#     queue_name = result.method.queue

#     channel.queue_bind(exchange=exchange_name,
#                        queue=queue_name, routing_key=binding_key)

#     print(
#         f" [*] Waiting for messages with routing key '{binding_key}'. To exit press CTRL+C")

#     channel.basic_consume(
#         queue=queue_name, on_message_callback=callback, auto_ack=True)

#     channel.start_consuming()

# Example usage
# receive_messages("*.messages")
