from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, default='')
    created_datetime = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=64, default='')
    content = models.TextField(default='')

    def __str__(self):
        return f'Username: {self.username} | Title: {self.title}'
