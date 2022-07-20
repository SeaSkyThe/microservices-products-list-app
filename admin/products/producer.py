import pika, json

params = pika.URLParameters("amqps://zrtzvwlx:aJ47ugn5XMiilSgbxNFjCjisbwJhoLuz@gull.rmq.cloudamqp.com/zrtzvwlx")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)