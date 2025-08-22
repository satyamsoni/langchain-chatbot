# server.py
from fastapi import FastAPI, WebSocket
from chatbot import Chatbot
import uvicorn

app = FastAPI()

@app.websocket("/ws/chat")
async def chat_ws(websocket: WebSocket):
    await websocket.accept()
    bot = Chatbot()

    try:
        while True:
            user_input = await websocket.receive_text()
            async for chunk in bot.chain.astream(
                {"input": user_input},
                config={"configurable": {"session_id": bot.session_id}}
            ):
                await websocket.send_text(chunk.content)

            await websocket.send_text("[[END]]")
    except Exception as e:
        await websocket.close()
        print(f"WebSocket closed: {e}")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
