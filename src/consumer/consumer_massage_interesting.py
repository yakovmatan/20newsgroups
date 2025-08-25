from src.kafka_configurations import Configurations

class ConsumerMassageInteresting:

    def __init__(self, topic='interesting'):
        self.event = Configurations().get_consumer_events(topic)

    def consumer_with_auto_commit(self):
        self.print_messages(self.event)


    def print_messages(self,events):
        for message in events:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))