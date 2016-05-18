from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Show

def index(request):
    show = Show.objects.all()
    templ = loader.get_template('shows/shows_index.html')
    context = {'show': show}

    return HttpResponse(templ.render(context, request))

def view_show(request, show_id):
    try:
        show = Show.objects.get(id=show_id)
    except Show.DoesNotExist:
        raise Http404("No such show!")
    context = {'show': show}

    return render(request, 'shows/show_details.html', context)
