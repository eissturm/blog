from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    body_raw = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User')

    class Meta:
        verbose_name_plural = "entries"

    
    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.published = True
        self.save()

class Comment(models.Model):
    body_raw = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    def __str__(self):
        return self.body_raw[:20] + "... | " + self.entry.title[:20] + " - By " + self.entry.author.username
