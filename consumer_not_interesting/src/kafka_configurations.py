import os
from kafka import KafkaProducer,KafkaConsumer
import json

class Configurations:

    def __init__(self):
        self.bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS", 'localhost:9092')


    def get_consumer_events(self,topic):
        consumer = KafkaConsumer(topic,
                                 group_id='not-interesting',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=[self.bootstrap_servers],
                                 consumer_timeout_ms=10000)
        return consumer



