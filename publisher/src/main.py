from fastapi import FastAPI
from publisher.src.producer_messege import ProducerMessage

app = FastAPI()

producer = ProducerMessage()

@app.get("/publish_message")
def get_all_soldiers():
    try:
        producer.publish_message()
        return {
            "status": "success",
            "message": "Sent 20 messages to Kafka",
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }