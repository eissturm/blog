from rest_framework import serializers
from feed.models import Entry, Comment

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('url', 'author', 'title','body_raw', 'published', 'created_date', 'modified_date','published_date', 'comment_set')
