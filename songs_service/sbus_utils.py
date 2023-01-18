import pika
from django.conf import settings

def send_message(message, routing_key='songservice'):
    url = settings.AMQP_URL
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=routing_key, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Transient))

    print ("Message sent to consumer")
    connection.close()