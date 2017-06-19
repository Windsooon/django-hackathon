# docker-django-base

### Django + Django REST framework + Nginx + Gunicorn + Docker

### What is this
I used to spend a lot of time setup Django and Django REST framework...So this is a base project use to play around or hackerathon.
### How to use

1. Make sure your host 80 port is available
2. in your project directory, run 

        git clone git@github.com:Windsooon/django-hackathon.git
        cd django-hackathon/
        docker-compose up -d --build

    Now you can look at http://127.0.0.1/api/

![api_root](https://raw.githubusercontent.com/Windsooon/django-hackathon/master/imgs/apiroot.png)

and  http://127.0.0.1/api/inner/

![api_inner](https://raw.githubusercontent.com/Windsooon/django-hackathon/master/imgs/inner.png)


and  http://127.0.0.1/api/playlist/

![api_playlist](https://raw.githubusercontent.com/Windsooon/django-hackathon/master/imgs/playlist.png)

3. You can add what you need in requirements.txt
4. playlist->inner just like tracks->album, sorry for the confusion, there modals just like this:


        class Inner(models.Model):
        
            name = models.CharField(max_length=50)
            category = models.CharField(max_length=100)
            create_time = models.DateTimeField(auto_now_add=True)
            update_time = models.DateTimeField(auto_now=True)
        
            def __str__(self):
                return self.name
        
        class Playlist(models.Model):
        
            inner = models.ForeignKey(
                Inner, related_name="playlist", on_delete=models.CASCADE, null=True)
            name = models.CharField(max_length=50)
            real_id = models.CharField(max_length=50)
            channel_id = models.CharField(max_length=50)
            channel_title = models.CharField(max_length=100)
            description = models.CharField(max_length=500)
            thumbnails = models.URLField()
            create_time = models.DateTimeField(auto_now_add=True)
            update_time = models.DateTimeField(auto_now=True)
        
            def __str__(self):
                return self.name + " / " + self.channel_title
