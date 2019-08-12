import subprocess
import threading
def nmap(host):
    result = subprocess.run(
        'nmap - p 3306, 80 %s' % host,
        shell=True
    )

    print(result)
    # if result.returncode == 0:
    #     print('%s:up' % host)
    # else:
    #     print('%s:down' % host)

if __name__ == '__main__':
    ips = ['176.233.6.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=nmap, args=(ip,))
        t.start()


