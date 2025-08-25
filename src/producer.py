from kafka_configurations import Configurations


class Producer:

    def __init__(self):
        self.producer = Configurations().get_producer_config()


    def publish_message(self,topic,message):
        self.producer.send(topic, message)


    def publish_message_with_key(self,topic,key,message):
        self.producer.send(topic, key=key, value=message)

    def flush(self):
        self.producer.flush()


if __name__ == '__main__':
    producer = Producer()
    event = {"App":"Producer 1"}
    event_1 = {"App": "Producer 2"}

    #Publish message to a topic
    producer.publish_message("topic1",event)

    #Publish message to a topic with key to enable hashed partitioning
    producer.publish_message_with_key("topic1",b"client1",event_1)

    # block until all async messages are sent
    producer.flush()