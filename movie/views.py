from django.shortcuts import render, redirect, get_object_or_404
from user.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *

# Create your views here.
#! Custom 404 Sayfası için
def Page_404(request, exception):
    return render(request, '404/404_Page.html', {})

def index_view(request):
    if request.user.is_authenticated:
        return redirect('profiles_page')    
    return render(request, 'movie/index.html', {})

@login_required(login_url='/user/login/')
def movies_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug, owner=request.user)
    movies = Movies.objects.all()
    categories = Category.objects.all()
    genres = Genre.objects.all()
    profiles = request.user.profile_set.all()

    #! İzlenme sırasına göre film gösterme
    top_movies = Movies.objects.all().order_by('-view_count')

    q = request.GET.get('q')
    if q:
        filmler = Movies.objects.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q) |
            Q(genre__name__icontains=q)
        ).distinct()

        return render(request, 'movie/movies.html', {
            'categories': categories,
            'genres': genres,
            'profile': profile,
            'profiles': profiles,
            'filmler': filmler,
            'top_movies': top_movies,
        })

    return render(request, 'movie/movies.html', {
        'profile': profile,
        'movies': movies,
        'categories': categories,
        'genres': genres,
        'profiles': profiles,
        'top_movies': top_movies,
    })

@login_required(login_url='/user/login/')
def movie_video_view(request, movie_slug):
    movie = get_object_or_404(Movies, slug=movie_slug)
    movie.view_count += 1
    movie.save()

    return render(request, 'movie/video.html', {
        'movie': movie,
    })

@login_required(login_url='/user/login/')
def movies_type_view(request, profile_slug, slug):
    profile = get_object_or_404(Profile, slug=profile_slug, owner=request.user)
    movies_category = Movies.objects.filter(category__slug=slug)
    movies_genre = Movies.objects.filter(genre__slug=slug)

    categories = Category.objects.all()
    genres = Genre.objects.all()
    profiles = request.user.profile_set.all()

    return render(request, 'movie/movies.html', {
        'movies_category': movies_category,
        'movies_genre': movies_genre,
        'categories': categories,
        'genres': genres,
        'profile': profile,
        'profiles': profiles,
    })
