from publisher.src.data import Data
from publisher.src.producer import Producer


class ProducerMessage:

    def __init__(self):
        self.producer = Producer()
        self.data = Data()
        self.number_of_massage = 10

    def publish_message(self):
        self.producer.publish_message("interesting", self.data.get_newsgroups_interesting()[self.number_of_massage - 10:self.number_of_massage])
        self.producer.publish_message("not_interesting", self.data.get_newsgroups_not_interesting()[self.number_of_massage - 10:self.number_of_massage])
        self.number_of_massage += 10