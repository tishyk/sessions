import argparse

parser = argparse.ArgumentParser()

parser.add_argument('agent_ip', type=str, help="Agent IP address to obtaining the file system")
parser.add_argument('-p', '--port', action='store_const', const=3, help="Help for port key")
#                          ('--xml', action='store_true', help="Get xml data")
parser.add_argument('-ap', dest='password', type=str, help="Host 'root' password")
parser.add_argument('--master_ip', help=argparse.SUPPRESS)  # Hide master_ip option

mgrp = parser.add_mutually_exclusive_group()

mgrp.add_argument('--xml', action='store_true', help="Get xml data")
mgrp.add_argument('--html', action='store_true', help="Get html data")
mgrp.add_argument('--yaml', action='store_true', help="Get yaml data")
mgrp.add_argument('--json', action='store_true', help="Get json data")

parser.add_argument('--list',
                    const='all',
                    nargs='?',
                    choices=['servers', 'storage', 'all'],
                    help='list servers, storage, or both (default: %(default)s)')

args = parser.parse_args()
print(args.agent_ip, args.port)
print(args.master_ip)
