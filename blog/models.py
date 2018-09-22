from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True )
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        post_name = f'{self.title}'  # python version 3.6
        return post_name


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        tag_name = f'{self.title}'
        return tag_name