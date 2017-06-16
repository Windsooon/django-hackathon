from django.db import models


class Inner(models.Model):

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
