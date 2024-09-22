from django.shortcuts import render
from .models import movies
# Create your views here.
from django.core.paginator import Paginator

def movie_list(request):
    movie_objects=movies.objects.all()
    movie_name=request.GET.get('movie_name')


    if movie_name !='' and movie_name is not None:
        movie_objects=movie_objects.filter(name__icontains=movie_name)   


    paginator=Paginator(movie_objects,4)
    page=request.GET.get('page')
    movie_objects=paginator.get_page(page)
    return render(request,'app/movie_list.html',{'movie_objects':movie_objects})