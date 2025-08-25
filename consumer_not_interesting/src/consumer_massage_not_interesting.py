from datetime import datetime, timezone
from consumer_not_interesting.src.kafka_configurations import Configurations
from consumer_not_interesting.src.mongodb_connection import DbConnection


class ConsumerMassageNotInteresting:

    def __init__(self, topic='not_interesting'):
        self.events = Configurations().get_consumer_events(topic)
        self.connection = DbConnection()
        self.collection = self.connection.db[topic]

    def consumer_with_auto_commit(self):
        self.insert_to_mongodb(self.events)


    def insert_to_mongodb(self,events):
        for message in events:
            try:
                data = message.value

                data["created_at"] = datetime.now(timezone.utc)

                self.collection.insert_one(data)
                return f"Message inserted: {data}"
            except Exception as e:
                return f"❌ Failed to insert message: {e}"