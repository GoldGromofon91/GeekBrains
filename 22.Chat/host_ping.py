import subprocess


def host_ping(ip):
    print('Hosts:\n',ip)
    for idx,el in enumerate(ip,1):
        proc_1 = subprocess.Popen(f'ping {el} -c 3 -W 2',shell=True,stdout=subprocess.DEVNULL)
        proc_1.wait()
        print(f'{idx}. Host {el} - reachable 'if not proc_1.poll() else f'{idx}. Host {el} - unreachable')


host_name = ['google.com','ya.ru','gb.ru']
host_ping(ip=host_name)