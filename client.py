import asyncio
import websockets

async def listen():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Terhubung ke server...")

        while True:
            message = await websocket.recv()
            print("Data diterima:", message)

asyncio.run(listen())