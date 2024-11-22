from socket_lib import TCPServer

def echo_handler(conn, addrinfo):
    ins, outs = conn.makefile("r"), conn.makefile("w")
    try:
        for line in ins:
            print(f"Client[{addrinfo}] sent: {line}")
            print(line.upper(), file=outs, flush=True)
            if "exit" in line:
                break
    except ConnectionResetError:
        print("Client closed the connection...")
    finally:
        ins.close()
        outs.close()    


if __name__ == '__main__':
    try:
        with TCPServer("localhost", 6789, echo_handler, worker="gevent") as server:
            server.run_forever()

    except KeyboardInterrupt:
        server.shutdown()
