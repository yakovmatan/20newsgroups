import os
from kafka import KafkaProducer
import json

class Configurations:

    def __init__(self):
        self.bootstrap_servers = os.getenv("KAFKA_BROKER", 'localhost:9092')


    def get_producer_config(self):
        producer = KafkaProducer(bootstrap_servers=[self.bootstrap_servers],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer