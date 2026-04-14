import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    print("Client terhubung")

    try:
        async for message in websocket:
            print("Data diterima dari scraper:")
            print(message)

            for client in clients:
                await client.send(message)

    except:
        print("Client terputus")

    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server berjalan di ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())