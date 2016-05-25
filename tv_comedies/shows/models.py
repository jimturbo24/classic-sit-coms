from django.db import models
from django.contrib.auth.models import User
from datetime import date
from dateutil.relativedelta import relativedelta

class ShowManager(models.Manager):
    def show_count(self):
        return self.count()

class Show(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=False, blank=False)
    tag = models.SlugField(null=False, db_index=True)
    release_date = models.DateField(auto_now=True)
    country = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    tv_rating = models.CharField(max_length=128)
    production_co = models.CharField(max_length=128)
    objects = ShowManager()

    def is_kid_friendly(self):
        return self.tv_rating in ('TV-Y', 'TV-Y7', 'G')

    def __str__(self):
        return self.title

class Season(models.Model):
    name = models.PositiveIntegerField(null=False, default=0)
    total_episodes = models.PositiveIntegerField(null=False, default=0)
    beginning_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)

class Episode(models.Model):
    name = models.CharField(max_length=128)
    air_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=False, blank=False)
    director = models.OneToOneField('Director', null=True)
    writers = models.ManyToManyField('Writer')
    characters = models.ManyToManyField('Character')
    length = models.PositiveSmallIntegerField(null=False, default=0)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=128)
    bio = models.TextField(null=False, blank=False)
    actor = models.OneToOneField('Actor', null=True)
    show = models.ForeignKey('Show')

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=128)
    birth_day = models.DateField(auto_now=False, default=date.today)
    bio = models.TextField(null=False, blank=False)

    @property
    def age(self):
        return relativedelta(date.today(), self.birth_day)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=128)
    birth_day = models.DateField(auto_now=False, default=date.today)
    bio = models.TextField(null=False, blank=False)

    @property
    def age(self):
        return relativedelta(date.today(), self.birth_day)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_text = models.TextField(max_length=2000, blank=False)
    user_rating = models.PositiveIntegerField(default=0, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    show = models.ForeignKey(Show, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now=True)

    def trans_rate(self):
        if self.user_rating < 3:
            return 'Bad'
        elif self.user_rating > 7:
            return 'Great'
        else:
            return 'Good'

    def __str__(self):
        return str(self.user) + ": " + str(self.show)

class Writer(models.Model):
    name = models.CharField(max_length=128)
    bio = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
