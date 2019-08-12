import paramiko

def ssh_host(host, user, passwd, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko)
    ssh.connect('%s',username='%s', password='%s', port='%s' % (host, user, passwd, port))

if __name__ == '__main__':
    ssh_host('192.168.1.23', 'root', 'a', '22')