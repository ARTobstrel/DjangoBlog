from time import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts',
                                  blank=True)  # blank=True означает что это поле необязательное к заполнению
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug': self.slug})

    def __str__(self):
        post_name = f'{self.title}'  # python version 3.6
        return post_name

    class Meta:
        ordering = ['-date_pub'] #отображения списка постов от свежего до старого


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        tag_name = f'{self.title}'
        return tag_name

    class Meta:
        ordering = ['title'] # отображает теги по алфавиту