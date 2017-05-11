from django.contrib import admin

# Register your models here.
from .models import Entry, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class EntryAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment)
