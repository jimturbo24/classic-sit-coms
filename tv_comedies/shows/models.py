from django.db import models
from django.contrib.auth.models import User


class Show(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=False, blank=False)
    tag = models.SlugField(null=False, db_index=True)
    release_date = models.DateField()
    country = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    tv_rating = models.CharField(max_length=128)
    production_co = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Season(models.Model):
    name = models.PositiveIntegerField(null=False, default=0)
    total_episodes = models.PositiveIntegerField(null=False, default=0)
    beginning_date = models.DateField()
    end_date = models.DateField()

class Episode(models.Model):
    name = models.CharField(max_length=128)
    air_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=False, blank=False)
    director = models.OneToOneField('Director', null=True)
    writer = models.CharField(max_length=128)
    characters = models.ManyToManyField('Character')
    length = models.PositiveSmallIntegerField(null=False, default=0)

class Character(models.Model):
    name = models.CharField(max_length=128)
    bio = models.TextField(null=False, blank=False)
    actor = models.OneToOneField('Actor', null=True)
    show = models.ForeignKey('Show')

class Actor(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField(null=False, default=0)
    bio = models.TextField(null=False, blank=False)

class Director(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField(null=False, default=0)
    bio = models.TextField(null=False, blank=False)

class Review(models.Model):
    review_text = models.TextField(max_length=2000, blank=False)
    user_rating = models.PositiveIntegerField(default=0, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    show = models.ForeignKey(Show, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now=True)
