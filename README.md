SocketIo broadcast Server
Overview

This project implements a WebSocket echo server using FastAPI and Socket.IO. It allows brodcasting messages  between clients and the server in real-time. Any message sent by a client is echoed back to all connected clients.
Installation

To install the required dependencies, run:

Linux: python3 -m venv env

source env/bin/activate

pip install fastapi uvicorn python-socketio pytest httpx

bash

pip install -r requirements.txt

Running the Server

Start the server by running:

bash

uvicorn main:app --host 0.0.0.0 --port 8000

Running Tests

Execute unit tests with:

bash

pytest test_main.py

Functionality

    WebSocket Endpoint (/ws):
        Handles client connections, echoing received messages to all connected clients.
        handles errors and client disconnections.
    Socket.IO Events:
        Welcomes clients upon connection and logs disconnections.
    Unit Tests:
        Verify single message echoing, multiple messages handling, and large message transmission.

