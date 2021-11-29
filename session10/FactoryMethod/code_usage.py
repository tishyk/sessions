from fam import SSH

ssh = SSH.get_connection(com=21)
ssh.connect()
ssh.call('ls -l')
ssh.close()