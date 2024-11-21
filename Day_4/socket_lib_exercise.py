from socket_lib import TCPServer

def echo_handler(conn, addrinfo):
    pass # TODO


if __name__ == '__main__':
    server = TCPServer("localhost", 6789, echo_handler)
    server.start()
    