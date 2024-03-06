from fastapi import FastAPI, WebSocket
from socketio import AsyncServer
from starlette.testclient import TestClient
app = FastAPI()
sio = AsyncServer(async_mode='asgi')

clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            for client in clients:
                await client.send_text(data)
    except Exception as e:
        print("WebSocket Error:", e)
    finally:
        clients.remove(websocket)

@sio.on('connect')
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    await sio.emit('message', 'Welcome to the server!', room=sid)

@sio.on('disconnect')
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

def test_websocket_endpoint():
    client = TestClient(app)

    with client.websocket_connect("/ws") as websocket:
        assert websocket.accept()

        websocket.send_text("Hello, server!")

        response = websocket.receive_text()
        assert response == "Echoed: Hello, server!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
