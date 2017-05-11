from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Entry
from .serializers import EntrySerializer

# Create your views here.
def index(request):
    return HttpResponse("Hola!")

def list_entries(request):
    return HttpResponse("Your list of entries")

def entry_detail(request, entry_id):
    return HttpResponse("Entry detail page for {}".format(entry_id))

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
