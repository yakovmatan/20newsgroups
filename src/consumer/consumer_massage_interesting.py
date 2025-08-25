from src.MongoDB.mongodb_connection import DbConnection
from src.kafka_configurations import Configurations
from datetime import datetime, timezone

class ConsumerMassageInteresting:

    def __init__(self, topic='interesting'):
        self.event = Configurations().get_consumer_events(topic)
        self.connection = DbConnection()
        self.collection = self.connection.db[topic]

    def consumer_with_auto_commit(self):
        self.insert_to_mongodb(self.event)


    def insert_to_mongodb(self,events):
        for message in events:
            try:
                data = message.value  # כבר dict בגלל value_deserializer

                # הוספת חותמת זמן
                data["created_at"] = datetime.now(timezone.utc)

                self.collection.insert_one(data)
                return f"Message inserted: {data}"
            except Exception as e:
                return f"❌ Failed to insert message: {e}"
