server {

    listen 80;
    server_name stage.youtubeplaylist.com;
    charset utf-8;

    location /static {
        add_header Cache-Control no-cache;
        expires -1;
        sendfile off;
        alias /usr/src/app/static;
    }

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
    }

}
