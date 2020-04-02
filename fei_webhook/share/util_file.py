from main_settings.settings import BASE_DIR
import os
import datetime

FILENAME = 'github_webhook.log'
GITHUB_LOGFILE = os.path.join(BASE_DIR, 'log', FILENAME)

def log_event(log_content):
    t = str(datetime.datetime.now()) + '\n'
    with open(GITHUB_LOGFILE, "a") as f:
        f.write('----------------------\n')
        f.write(t)
        f.write(log_content + '\n')

if __name__ == '__main__':
    log_event('abc')