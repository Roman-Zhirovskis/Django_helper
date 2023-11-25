import pika
import sys

class Subscriber:
    
    def __init__(self, queueName, bindingKey, config):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.config = config
        self.connection = self._create_connection()
        
    def __del__(self):
        self.connection.close()

    def _create_connection(self):
        parameters = pika.ConnectionParameters(host=self.config['host'], port=self.config['port'])
        return pika.BlockingConnection(parameters)
    
    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print("Received new message for - {}".format(binding_key))

    def setup(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'], exchange_type='topic')
        channel.queue_declare(queue=self.queueName)
        channel.queue_bind(queue=self.queueName, exchange=self.config['exchange'], routing_key=self.bindingKey)
        channel.basic_consume(queue=self.queueName, on_message_callback=self.on_message_callback, auto_ack=True)
        print("[*] Waiting for data for {}. To exit press CTRL+C".format(self.queueName))
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            
config = {'host': 'localhost', 'port': 5672, 'exchange': 'my_exchange'}
if len(sys.argv) < 3:
    print("Usage: {} <QueueName> <BindingKey>".format(__file__))
    sys.exit()
else:
    queueName = sys.argv[1]
    key = sys.argv[2]  # key in the form exchange.*
    subscriber = Subscriber(queueName, key, config)
    subscriber.setup()