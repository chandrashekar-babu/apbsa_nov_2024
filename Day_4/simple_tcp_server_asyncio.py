import asyncio

async def create_tcp_server(addr, port, handler_fn):
    server = await asyncio.start_server(handler_fn, addr, port)

    #addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}:{port}')

    async with server:
        await server.serve_forever()



async def echo_handler(reader, writer):
    print(writer, reader)
    writer.write(b"Welcome to async capable echo server...\n")
    await writer.drain()

    while True:
        data = await reader.readline()
        message = data.decode()
        addr = writer.get_extra_info('peername')
        
        print(f"Received {message!r} from {addr!r}")
        print(f"Send: {message!r}")
        
        writer.write(data.upper())
        await writer.drain()
        if "exit" in message:
            break

    print(f"Closing connection for {writer.get_extra_info('peername')}")
    writer.close()


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    asyncio.run(create_tcp_server(args.host, args.port, echo_handler))

