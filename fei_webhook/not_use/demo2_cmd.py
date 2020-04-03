import os
import subprocess

DIR = '/Users/pengfei/Documents/temp'

def func(directory):
    os.chdir(directory)
    subprocess.call(["ls", "-l"])

if __name__ == '__main__':
    func(DIR)