import asyncio

async def create_tcp_connection(addr, port, handler_fn):
    reader, writer = await asyncio.open_connection(addr, port)    
    await handler_fn(reader, writer)

async def echo_client(reader, writer):
    print(f"Established connection to {writer.get_extra_info('peername')}")
    
    while True:
        data = await reader.readline()
        message = data.decode()
        addr = writer.get_extra_info('peername')
        
        print(f"Received {message!r} from {addr!r}")
        
        line = input("Enter message: ")
        writer.write(line.encode())
        print("wrote message. Draining..")
        await writer.drain()
        if "exit" in line:
            break

    print(f"Closing connection for {writer.get_extra_info('peername')}")
    writer.close()

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    asyncio.run(create_tcp_connection(args.host, args.port, echo_client))

