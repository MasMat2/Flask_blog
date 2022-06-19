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

sudo apt install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow 5000
sudo ufw enable

---

setup config file
export FLASK_APP
flask run --host=0.0.0.0
sudo apt install nginx
pip install gunicorn

sudo rm /etc/nginx/sites-enabled/default

sudo nano /etc/nginx/sites-enabled/flaskblog
server {
        listen 80;
        server_name 198.58.104.79;

        location /static {
                alias /home/max/Flask_blog/flaskblog/static;
        }

        location / {
                proxy_pass http://localhost:8000;
                include /etc/nginx/proxy_params;
                proxy_redirect off;
        }
}


sudo ufw allow http/tcp
sudo ufw delete allow 5000
sudo ufw enable
sudo ufw status
sudo systemctl restart nginx

sudo bindfs -u www-data -g www-data /home/max/Flask_blog/flaskblog/static /usr/share/nginx/static
location /static {
                alias /usr/share/nginx/static;
}
sudo systemctl restart nginx

gunicorn -w 3 run:app

sudo apt install supervisor

sudo nano /etc/supervisor/conf.d/flaskblog.conf
[program:flaskblog]
directory=/home/max/Flask_blog
command=/home/max/environments/Flask_blog/bin/gunicorn -w 3 run:app
user=max
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flaskblog/flaskblog.err.log
stdout_logfile=/var/log/flaskblog/flaskblog.out.log

sudo mkdir -p /var/log/flaskblog/
sudo touch /var/log/flaskblog/flaskblog.err.log
sudo touch /var/log/flaskblog/flaskblog.out.log

sudo supervisorctl reload

sudo nano /etc/nginx/nginx.conf
http {
        client_max_boy_size 5M;
}

sudo supervisorctl reload