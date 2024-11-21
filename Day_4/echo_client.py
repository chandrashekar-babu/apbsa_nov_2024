from argparse import ArgumentParser
from socket_lib import create_client, echo_client

parser = ArgumentParser()
parser.add_argument("port", type=int)

args = parser.parse_args()

create_client("localhost", args.port, echo_client)
