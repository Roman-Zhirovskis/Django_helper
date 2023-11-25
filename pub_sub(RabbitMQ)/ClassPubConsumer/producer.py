import pika

class Publisher:
  
    def __init__(self, config):
        self.config = config
        
    def publish(self, routing_key, message):
        connection = self.create_connection()
        channel = connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'], exchange_type='topic')
        channel.basic_publish(exchange=self.config['exchange'], routing_key=routing_key, body=message)
        print(" [x] Sent message %r for %r" % (message,routing_key))
        connection.close()
        
    def create_connection(self):
        param = pika.ConnectionParameters(host=self.config['host'], port=self.config['port']) 
        return pika.BlockingConnection(param)
    
config = {'host': 'localhost', 'port': 5672, 'exchange': 'my_exchange'}
publisher = Publisher(config)
publisher.publish('nse.nifty', 'New Data')
