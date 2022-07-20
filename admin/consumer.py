import django
django.setup()

import json, os 
import pika
from products.models import Product



params = pika.URLParameters("amqps://zrtzvwlx:aJ47ugn5XMiilSgbxNFjCjisbwJhoLuz@gull.rmq.cloudamqp.com/zrtzvwlx")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(channel, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()