from fastapi import FastAPI, HTTPException
import uvicorn as uv
from consumer_massage_not_interesting import ConsumerMassageNotInteresting

app = FastAPI()

consumer = ConsumerMassageNotInteresting()

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
    uv.run('main:app', host='127.0.0.1', port=8001, reload=True)