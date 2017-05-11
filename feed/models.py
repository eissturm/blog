from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    body_raw = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User)

class Comment(models.Model):
    body_raw = models.TextField()
    author = models.ForeignKey(User)
    entry = models.ForeignKey(Entry)

    
