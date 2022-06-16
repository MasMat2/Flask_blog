apt update && apt upgrade
hostnamectl set-hostname flask-server

# /etc/hosts
127.0.0.1       localhost
198.58.104.79   flask-server

adduser max

adduser max sudo

exit

fake@
ssh-keygen -b 4096
scp ~/.ssh/id_rsa.pub max@198.58.104.79:~/.ssh/authorized_keys

server@
sudo chmod 700 .ssh
sudo chmod 600 .ssh/*

sudo nano /etc/ssh/sshd_config
    PermitRootLogin no
    PasswordAuthentication no

sudo systemctl restart sshd

