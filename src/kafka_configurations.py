import os
from kafka import KafkaProducer,KafkaConsumer
import json

class Configurations:

    def __init__(self):
        self.bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS", 'localhost:9092')


    def get_producer_config(self):
        producer = KafkaProducer(bootstrap_servers=[self.bootstrap_servers],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer


    def get_consumer_events(self,topic):
        consumer = KafkaConsumer(topic,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=[self.bootstrap_servers],
                                 consumer_timeout_ms=10000)
        return consumer



