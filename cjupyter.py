#!/anaconda/bin/python
import subprocess as sp
import sys
import os

envs = os.listdir('/anaconda/envs/')
envs = [x for x in envs if x[0] != '.']

assert sys.argv[1] in envs

path = "/anaconda/envs/{}".format(sys.argv[1])

python_version = [x for x in os.listdir('{}/lib'.format(path)) if 'python' in x and not 'lib' in x][0]

jpath = "{}/bin/jupyter".format(path)
lpath = "{}/lib/{}/site-packages/jupyterlab".format(path, python_version)
if os.path.exists(jpath) and os.path.exists(lpath):
    running = sp.check_output(['running_labs'])
    running = running.lstrip().rstrip().split('\n')
    if sys.argv[1] not in running:
        sp.Popen(args=['jlab_start {} {}'.format(jpath, sys.argv[1])], shell=True)
    else:
        print(u'\u001b[33m Jupyter lab already running in enviroment {}\u001b[0m'.format(sys.argv[1]))
else:
    print(u'\u001b[31m Jupyter not installed in conda env {}\u001b[0m'.format(sys.argv[1]))
