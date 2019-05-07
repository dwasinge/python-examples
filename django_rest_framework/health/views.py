from django.shortcuts import render

from django.http import HttpResponse
from people.models import Person

def health(request):
    return HttpResponse(Person.objects.count())
