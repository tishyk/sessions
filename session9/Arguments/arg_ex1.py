import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('ip', help="Help for ip parameter")
parser.add_argument('-p', '--port', type=str, default='10.10.0.27', help="Help for port key")
parser.add_argument("--system_id", dest="id", type=int, default=0,
                    help="Enter system id from the local network (Ex. 15446)")


args = parser.parse_args()

args.ip  # 10.151.58.15
args.port  # 10.151.15.15
args.id  # 10.151.15.15

time.sleep(12500)