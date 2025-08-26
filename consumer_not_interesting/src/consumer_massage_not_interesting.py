from datetime import datetime, timezone
from kafka_configurations import Configurations
from mongodb_connection import DbConnection


class ConsumerMassageNotInteresting:

    def __init__(self, topic='not_interesting'):
        self.events = Configurations().get_consumer_events(topic)
        self.connection = DbConnection()
        self.collection = self.connection.db[topic]

    def consumer_with_auto_commit(self):
        return self.insert_to_mongodb(self.events)


    def insert_to_mongodb(self,events):
        inserted = []
        for messages in events:
            for m in messages.value:
                data = {}
                data['massege'] = m

                data["created_at"] = datetime.now(timezone.utc)

                self.collection.insert_one(data)
                inserted.append(data)
        return {"inserted": inserted}

    def find_all(self):
        try:
            return list(self.collection.find({}, {"_id": 0}))
        except Exception as e:
            return {"error": e}