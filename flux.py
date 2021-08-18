import os
import subprocess
import sys

class flux():

    def __init__(self, args):
        self.run = './fluxploider'
        self.args = args
        self.git = 'https://github.com/Flab-E/fuxploider'
        self.main()

    def main(self):
        if ('fuxploider.py' not in os.listdir()):
            clone_flux = subprocess.Popen(['git', 'clone', self.git], stdout = subprocess.PIPE)
            print(clone_flux)

        p = subprocess.Popen([self.run]+[self.args.split()], stdout = subprocess.PIPE)
        print(p.communicate())

inst = flux(sys.args)