from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):

    event_name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    participant = models.ManyToManyField(User)
    maximum_participants = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.event_name