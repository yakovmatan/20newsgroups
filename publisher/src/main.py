from fastapi import FastAPI
from producer_messege import ProducerMessage
import uvicorn as uv

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

if __name__ == '__main__':
    uv.run('main:app', host='127.0.0.1', port=8002, reload=True)