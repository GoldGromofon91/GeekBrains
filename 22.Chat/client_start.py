import os
import subprocess

from os.path import dirname, abspath, join

CHAT_DIR = abspath(join(dirname(os.path.abspath(__file__)), 'chat'))


def start():
    print(CHAT_DIR)
    print('Client start')
    server_proc = subprocess.Popen(['python', f'{CHAT_DIR}/client.py'], shell=True, stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    server_proc.wait()
    our, err = server_proc.communicate()
    print(err)


if __name__ == "__main__":
    print('Client Connected')
    start()
