from starlette.testclient import TestClient
from main import app

def test_websocket_endpoint():
    client = TestClient(app)

    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("Hello, server!")

        response = websocket.receive_text()
        assert response == "Hello, server!"

def test_websocket_endpoint_multiple_messages():
    client = TestClient(app)

    with client.websocket_connect("/ws") as websocket:
        # Send multiple messages to the server
        messages = ["Message 1", "Message 2", "Message 3"]
        for msg in messages:
            websocket.send_text(msg)

        # Receive the echoed messages from the server
        for msg in messages:
            response = websocket.receive_text()
            assert response == f"{msg}"

def test_websocket_endpoint_large_message():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        # Send a large message to the server
        large_message = "a" * 100000  # Creating a large string
        websocket.send_text(large_message)

        # Receive the echoed message from the server
        response = websocket.receive_text()
        assert response == f"{large_message}"