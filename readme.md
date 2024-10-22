Task1 Completed!
Task2 Completed!
Task3 Completed!
Task4 Completed!

http://159.89.16.182:8080/



/etc/nginx/sites-enabled/(nginx_file_nomi)

server {
    listen       8;
    server_name  159.89.16.182;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /var/www/exam8;
    }

    location /media/ {
        root /var/www/exam8;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/exam8/exam.sock;
    }

}







/etc/systemd/system/(service_fayl_nomi).service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/exam8
ExecStart=/var/www/exam8/env/bin/gunicorn --workers 3 --bind unix:/var/www/exam8/exam.sock config.wsgi:application

[Install]
WantedBy=multi-user.target



systemctl start (service_fayl_nomi).service
systemctl enable (service_fayl_nomi).service


