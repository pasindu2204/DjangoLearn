from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'movies/index.html', {'movie':'Monster'})

def about(request):
    return render(request, 'movies/about.html', {})    

    #app/templete/app/index.htmal
    #movies/templetes/movies/index.html