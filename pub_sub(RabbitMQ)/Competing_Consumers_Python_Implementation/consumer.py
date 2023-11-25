import time
import random

import pika

# Создается функция on_message_received, которая будет вызываться каждый раз при получении нового сообщения.
def on_message_received(ch, method, properties, body):
    # Генерируется случайное время processing_time на обработку сообщения.
    processing_time = random.randint(1, 6)
    # Выводится на экран информация о получении нового сообщения и времени на обработку.
    print(f'received: "{body}", will take {processing_time} to process')
    # Выполняется задержка processing_time для имитации обработки сообщения.
    time.sleep(processing_time)
    # Выполняется подтверждение обработки сообщения.
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # Выводится на экран информация об успешной обработке сообщения и подтверждении.
    print(f'finished processing and acknowledged message')

# Создаются параметры соединения connection_parameters для подключения к локальному хосту ('localhost').
connection_parameters = pika.ConnectionParameters('localhost')

# Создается соединение connection с использованием параметров connection_parameters.
connection = pika.BlockingConnection(connection_parameters)

# Создается канал channel для общения с брокером сообщений (RabbitMQ).
channel = connection.channel()

# Создается очередь 'letterbox' с помощью метода queue_declare.
channel.queue_declare(queue='letterbox')

# Устанавливается настройка basic_qos на предварительное получение одного сообщения для каждого потребителя (prefetch_count=1).
channel.basic_qos(prefetch_count=2)

# Устанавливается функция on_message_received для получения сообщений из очереди 'letterbox'.
channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

# Выводится сообщение о начале процесса получения сообщений (Starting Consuming).
print('Starting Consuming')

# Запускается процесс получения сообщений в бесконечном цикле с помощью метода start_consuming.
channel.start_consuming()
