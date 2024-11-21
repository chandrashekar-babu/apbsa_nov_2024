from simple_tcp_server import create_tcp_connection

def echo_client(conn, addr, port):
    print(f"Established connection to {addr}:{port}")
    
    with conn.makefile("w") as outs, conn.makefile("r") as ins:
        while True:
            reply = ins.readline()
            print("Server replies: ", reply)
            line = input("Enter message: ")
            print(line.strip(), file=outs, flush=True)
            if "exit" in line:
                break

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    create_tcp_connection(args.host, args.port, echo_client)

