from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import cv2
import base64
import asyncio
from pathlib import Path
import uvicorn


app = FastAPI()
clients = []

@app.websocket("/ws")
async def websocket_endppoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            data= await websocket.receive_text

            for client in clients:
                if client != websocket:
                    await client.send_text(data)
                
    except:
        client.remove(websocket)

@app.get("/")
def get():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read(), status_code=200)