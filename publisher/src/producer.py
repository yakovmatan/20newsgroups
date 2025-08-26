from kafka_configurations import Configurations


class Producer:

    def __init__(self):
        self.producer = Configurations().get_producer_config()


    def publish_message(self,topic,message):
        self.producer.send(topic, message)
        self.producer.flush()

    def publish_message_with_key(self,topic,key,message):
        self.producer.send(topic, key=key, value=message)
        self.producer.flush()