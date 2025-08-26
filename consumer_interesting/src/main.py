from fastapi import FastAPI, HTTPException
from consumer_interesting.src.consumer_massage_interesting import ConsumerMassageInteresting
import uvicorn as uv

app = FastAPI()

consumer = ConsumerMassageInteresting()

@app.get("/consumer_message")
def get_all_soldiers():
    result = consumer.consumer_with_auto_commit()
    if isinstance(result, dict) and "message" in result:
        return {
            "status": "failed",
            "error": result["message"]
        }

    return {
        "status": "success",
        "message": "Send 10 messages to mongodb",
    }


@app.get("/get_data")
def get_all_soldiers():
    result = consumer.find_all()
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=500, detail="Database error")
    return result

if __name__ == '__main__':
    uv.run('main:app', host='127.0.0.1', port=8000, reload=True)