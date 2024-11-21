from argparse import ArgumentParser
from socket_lib import create_server, echo_server, EchoHandler

parser = ArgumentParser()
parser.add_argument("port", type=int)

args = parser.parse_args()

create_server("localhost", args.port, EchoHandler)
