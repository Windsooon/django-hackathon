from django.db import models


class Playlist(models.Model):
    CATEGORY_CHOICES = (
            (0, 'EDUCATION'),
            (1, 'TALKSHOW'),
            (2, 'GAMES'),
    )

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
