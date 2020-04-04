import os
import subprocess

DIR = '/Users/pengfei/Documents/temp'

def func(directory):
    os.chdir(directory)
    subprocess.call(["ls", "-l"])

def func1(cmd):
    try:
        output = subprocess.check_output(cmd)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output.decode('utf-8'))
    except FileNotFoundError as e:
        print('wrong error')


if __name__ == '__main__':
    # func(DIR)
    cmd = ['grep', 'txt', 'abc.txt']
    func1(cmd)