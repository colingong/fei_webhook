"""执行shell cmd

"""
from subprocess import Popen, PIPE
from main_settings.settings import REPOS_PARENT_DIR

class Cmds(object):
    def __init__(self, cmds):
        self.cmds = cmds
        self.repos_parent_dir = REPOS_PARENT_DIR
    
    def run(self):
        process = Popen('bash', shell=False, universal_newlines=True,
        stdin=PIPE, stdout=PIPE, stderr=PIPE)
        for cmd in self.cmds:
            process.stdin.write(cmd + '\n')
        process.stdin.close()
        out = process.stdout.read()
        err = process.stderr.read()
        return out, err

if __name__ == '__main__':
    from ..main_settings.settings import BASE_DIR
    cmds = [
        # ['ls', '-l'],
        'pwpd',
        'cd ../..',
        'pwd ',
        'cd ' + BASE_DIR,
        'pwd',
        'cd not_use',
        'pwd',
        # ['ls', '-l'],
    ]

    r = ExcuteCmds(cmds)
    out, err = r.run()
    print(out)
    print(err)
    # r.__call__()
    # print(r.__call__())