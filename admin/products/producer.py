import pika

params = pika.URLParameters("amqps://zrtzvwlx:aJ47ugn5XMiilSgbxNFjCjisbwJhoLuz@gull.rmq.cloudamqp.com/zrtzvwlx")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')