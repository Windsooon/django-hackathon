from django.db import models


class Inner(models.Model):
    CATEGORY_CHOICES = (
            (0, 'EDUCATION'),
            (1, 'TALKSHOW'),
            (2, 'GAMES'),
    )

    name = models.CharField(max_length=50)
    category = models.SmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
