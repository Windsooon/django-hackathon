# docker-django-base
Django + Django REST framework + Nginx + Gunicorn + Docker

### What is this
I used to spend a lot of time setup Django and Django REST framework...So this is a base project use to play around or hackerathon.
### How to use

1. Make sure your host 80 port is available
2. in your project directory, run 

        git clone git@github.com:Windsooon/django-hackathon.git
        cd django-hackathon/
        docker-compose up -d --build

    Now you can look at http://127.0.0.1/api/inner/


![work](https://raw.githubusercontent.com/Windsooon/django-hackathon/master/imgs/work.png)

3. You can add what you need in requirements.txt

