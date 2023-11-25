import time
import random

import pika
# Создаются параметры соединения connection_parameters для подключения к локальному хосту ('localhost').
connection_parameters = pika.ConnectionParameters('localhost')

# Создается соединение connection с использованием параметров connection_parameters.
connection = pika.BlockingConnection(connection_parameters)

# Создается канал channel для общения с брокером сообщений (RabbitMQ).
channel = connection.channel()

# Создается очередь 'letterbox' с помощью метода queue_declare.
channel.queue_declare(queue='letterbox')

# Создается переменная messageId, которая будет использоваться для подсчета количества отправленных сообщений.
messageId = 1

# Бесконечный цикл для отправки сообщений.
while(True):
    # Формируется сообщение message, которое содержит ссылку на уникальный идентификатор сообщения messageId.
    message = f"Sending Message from producer_2 with Id = {messageId}"

    # Отправляется сообщение channel.basic_publish в очередь с именем 'letterbox'.
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    # Выводится на экран информация о отправленном сообщении.
    print(f"sent message: {message}")
    
    time.sleep(random.randint(1, 4))

    messageId+=1