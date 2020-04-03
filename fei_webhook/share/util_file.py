import os
import datetime


def log_event(log_content, log_file):
    t = str(datetime.datetime.now()) + '\n'
    with open(log_file, "a") as f:
        f.write('----------------------\n')
        f.write(t)
        f.write(log_content + '\n')

class ChangeDir(object):
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

if __name__ == '__main__':
    # log_event('abc')
    pass
