import pika

params = pika.URLParameters("amqps://zrtzvwlx:aJ47ugn5XMiilSgbxNFjCjisbwJhoLuz@gull.rmq.cloudamqp.com/zrtzvwlx")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(channel, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()