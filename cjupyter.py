#!/anaconda/bin/python
from __future__ import print_function

import subprocess as sp
import sys
import os
import time
import socket
from contextlib import closing
import color_codes as cc
from notebook import notebookapp
import argparse

parser = argparse.ArgumentParser(description='Start Jupyter Lab in the current or any conda enviroment in the system')
parser.add_argument('enviroment', metavar='Env', type=str, nargs='?',
                    help='envirment to start jupyter lab in')

args = parser.parse_args()
req_env = args.enviroment

def get_good_port(start):
    servers = sp.check_output(['jupyter notebook list'], shell=True)
    used_ports = list()
    for server in servers.split('\n')[1:]:
        if server != '':
            port = int(server.split('/')[2].split(':')[1])
            used_ports.append(port)
    if not start in used_ports:
        return start
    else:
        return max(used_ports) + 1

def is_running(port):
    servers = list(notebookapp.list_running_servers())
    ports = [x['port'] for x in servers]
    return port in ports

envs = os.listdir('/anaconda/envs/')
envs = [x for x in envs if x[0] != '.']

if 'CONDA_DEFAULT_ENV' in os.environ and not req_env:
    acc_env = req_env if req_env else os.environ['CONDA_DEFAULT_ENV'] 
    assert acc_env in envs or acc_env == 'root'
    path = "/anaconda/envs/{}".format(acc_env)
elif 'CONDA_DEFAULT_ENV' not in os.environ and not req_env:
    acc_env = 'root'
    path = '/anaconda'
else:
    acc_env = req_env
    path = "/anaconda/envs/{}".format(acc_env)

python_version = [x for x in os.listdir('{}/lib'.format(path)) if 'python' in x and not 'lib' in x][0]
jpath = "{}/bin/jupyter".format(path)
lpath = "{}/lib/{}/site-packages/jupyterlab".format(path, python_version)

port = get_good_port(8888)
if os.path.exists(jpath) and os.path.exists(lpath):
    running = sp.check_output(['running_labs'])
    running = running.lstrip().rstrip().split('\n')
    if acc_env not in running:
        try:
            sp.Popen(args=['jlab_start {} {} {}'.format(jpath, acc_env, port)], shell=True)
            time.sleep(3)
            with open('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env), 'w') as port_log:
                port_log.write(str(port))
            try:
                sys.stdout.write(u'{}Jupyter Lab Running in enviroment {} (<ctrl-c> to stop): {}'.format(cc.GREEN, acc_env, cc.RESET))
                sys.stdout.flush()
                while is_running(port):
                    if not os.path.exists('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env)):
                        print('{}\nWarning! Log File has been removed by an external program{}'.format(cc.YELLOW, cc.RESET))
                        with open('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env), 'w') as port_log:
                            port_log.write(str(port))
                        print("{}Log file recoverd{}".format(cc.GREEN, cc.RESET))
                        sys.stdout.write(u'{}Jupyter Lab Running (<ctrl-c> to stop):{}'.format(cc.GREEN, cc.RESET))
                        sys.stdout.flush()
                    time.sleep(1)
                print('{}Warning! External Shutdown executed, jupyter no longer running{}'.format(cc.YELLOW, cc.RESET))
                if os.path.exists('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env)):
                    os.remove('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env))
                print('{}Clean Up Complete{}'.format(cc.GREEN, cc.RESET))

            except KeyboardInterrupt:
                print('\r')
                print(u'{}Interupt Recived{}'.format(cc.BLUE, cc.RESET))
                print(u'{}Closing Jupyter Lab{}'.format(cc.BLUE, cc.RESET))
                sp.Popen(args=['jupyter notebook stop {}'.format(port)], shell=True)
                time.sleep(5)
                os.remove('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env))
                print('{}Clean Up Complete{}'.format(cc.GREEN, cc.RESET))
        except:
            print(u'{}ERROR! An unkown error has occured, jupyter lab cannot be started in enviroment {}{}'.format(cc.RED, acc_env, cc.RESET))
            if os.path.exists('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(sys.argv[0])):
                os.remove('/Users/tboudreaux/.jupyter_logs/ports/{}'.format(acc_env))
            print('{}Clean Up Complete{}'.format(cc.GREEN, cc.RESET))

    else:
        print(u'{}Jupyter lab already running in enviroment {}{}'.format(cc.YELLOW, acc_env, cc.RESET))
else:
    print(u'{}Jupyter not installed in conda env {}{}'.format(cc.RED, acc_env, cc.RESET))

