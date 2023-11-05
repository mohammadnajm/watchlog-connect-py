from client import WebSocketClient
import asyncio

async def main():
    ws_client = WebSocketClient()

    await ws_client.connect()
    await ws_client.increment("first_metric")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())