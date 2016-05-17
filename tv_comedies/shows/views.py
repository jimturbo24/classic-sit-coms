from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Show

def index(request):
    show = Show.objects.all()
    templ = loader.get_template('shows/shows_index.html')
    context = {'show': show}

    return HttpResponse(templ.render(context, request))
