from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Show, Actor, Episode, Season, Character, Director, Review, Writer

@login_required
def show_index(request):
    showList = Show.objects.all()
    templ = loader.get_template('shows/shows_index.html')
    context = {'shows': showList}

    return HttpResponse(templ.render(context, request))

def show_view(request, show_id):
    try:
        show = Show.objects.get(id=show_id)
    except Show.DoesNotExist:
        raise Http404("No such show!")
    context = {'show': show}

    return render(request, 'shows/show_details.html', context)

def actor_index(request):
    actorList = Actor.objects.all()
    templ = loader.get_template('shows/actor_index.html')
    context = {'actors': actorList}

    return HttpResponse(templ.render(context, request))

def actor_view(request, actor_id):
    try:
        actor = Actor.objects.get(id=actor_id)
    except Actor.DoesNotExist:
        raise Http404("No such actor!")
    context = {'actor': actor}

    return render(request, 'shows/actor_details.html', context)

@login_required
def episode_index(request):
    episodeList = Episode.objects.all()
    templ = loader.get_template('shows/episode_index.html')
    context = {'episodes': episodeList}

    return HttpResponse(templ.render(context, request))

def episode_view(request, episode_id):
    try:
        episode = Episode.objects.get(id=episode_id)
    except Episode.DoesNotExist:
        raise Http404("No such episode!")
    context = {'episode': episode}

    return render(request, 'shows/episode_details.html', context)

def season_index(request):
    seasonList = Season.objects.all()
    templ = loader.get_template('shows/season_index.html')
    context = {'seasons': seasonList}

    return HttpResponse(templ.render(context, request))

def season_view(request, season_id):
    try:
        season = Season.objects.get(id=season_id)
    except Season.DoesNotExist:
        raise Http404("No such season!")
    context = {'season': season}

    return render(request, 'shows/season_details.html', context)

def character_index(request):
    characterList = Character.objects.all()
    templ = loader.get_template('shows/character_index.html')
    context = {'characters': characterList}

    return HttpResponse(templ.render(context, request))

def character_view(request, character_id):
    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        raise Http404("No such character!")
    context = {'character': character}

    return render(request, 'shows/character_details.html', context)

def director_index(request):
    directorList = Director.objects.all()
    templ = loader.get_template('shows/director_index.html')
    context = {'directors': directorList}

    return HttpResponse(templ.render(context, request))

def director_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404("No such director!")
    context = {'director': director}

    return render(request, 'shows/director_details.html', context)

def review_index(request):
    reviewList = Review.objects.all()
    templ = loader.get_template('shows/review_index.html')
    context = {'reviews': reviewList}

    return HttpResponse(templ.render(context, request))

def review_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        raise Http404("No such review!")
    context = {'review': review}

    return render(request, 'shows/review_details.html', context)

def writer_index(request):
    writerList = Writer.objects.all()
    templ = loader.get_template('shows/writer_index.html')
    context = {'writers': writerList}

    return HttpResponse(templ.render(context, request))

def writer_view(request, writer_id):
    try:
        writer = Writer.objects.get(id=writer_id)
    except Writer.DoesNotExist:
        raise Http404("No such writer!")
    context = {'writer': writer}

    return render(request, 'shows/writer_details.html', context)
