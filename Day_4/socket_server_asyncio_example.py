import asyncio

async def handle_connection(reader, writer):
    print(reader, writer)
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_connection, "127.0.0.1", 8765
    )

    addr = server.sockets[0].getsockname()
    print(f"Server listening on {addr}")
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())