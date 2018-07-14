#!/anaconda/bin/python
from __future__ import print_function

import subprocess as sp
import sys
import os
import time
import socket
from contextlib import closing
from notebook import notebookapp
import color_codes as cc
import argparse

parser = argparse.ArgumentParser(description='Start Jupyter Lab in the current or any conda enviroment in the system')
parser.add_argument('enviroment', metavar='Env', type=str, nargs='?',
                    help='envirment to start jupyter lab in')

args = parser.parse_args()
req_env = args.enviroment

def get_env_port(enviroment):
    servers = list(notebookapp.list_running_servers())
    ports = [x['port'] for x in servers]
    open_servers = os.listdir('/Users/tboudreaux/.jupyter_logs/ports')
    if enviroment in open_servers:
        with open('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(enviroment), 'r') as f:
            port = f.readline()
        port = int(port.lstrip().rstrip())
        if port in ports:
            return port
        else:
            return -2
    else:
        return -1

envs = os.listdir('/anaconda/envs/')
envs = [x for x in envs if x[0] != '.']

assert sys.argv[1] in envs

path = "/anaconda/envs/{}".format(sys.argv[1])

python_version = [x for x in os.listdir('{}/lib'.format(path)) if 'python' in x and not 'lib' in x][0]

port = get_env_port(sys.argv[1])
if port == -1:
    print(u'{}No Envoroment port file found for enviroment {}{}'.format(cc.RED, sys.argv[1], cc.RESET))
elif port == -2:
    print(u'{}Port for enviroment {} not found in running notebook servers {}'.format(cc.YELLOW, sys.argv[1], cc.RESET))
    os.remove('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(sys.argv[1]))
else:
    print(port)
    os.remove('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(sys.argv[1]))

