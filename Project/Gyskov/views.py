from django.shortcuts import render
from .models import Films,Category
from django.http import HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

def index(request):
    films = Films.objects.all()
    return render(request, "index.html", {"films": films})

def create(request):
    if request.method == "POST":
        film = Films()
        category = Category()
        category.name = request.POST.get('category')
        film.name = request.POST.get("name")
        film.date_out = request.POST.get("date_out")
        film.date_view = request.POST.get("date_view")
        film.actors = request.POST.get('actors')
        film.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        category = Category.objects.get(id=id)
        films = Films.objects.get(id=id)
        if request.method == "POST":  
            category.name = request.POST.get('category')
            films.name = request.POST.get("name")
            films.date_out = request.POST.get("date_out")
            films.date_view = request.POST.get("date_view")
            films.actors = request.POST.get('actors')
            films.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"films": films})
    except Films.DoesNotExist:
        return HttpResponseNotFound("<h2>Film not found</h2>")

def delete(request, id):
    try:
        films = Films.objects.get(id=id)
        films.delete()
        return HttpResponseRedirect("/")
    except Films.DoesNotExist:
        return HttpResponseNotFound("<h2>Film not found</h2>")

def create_category():
    Category.objects.create(name = "horror")
    Category.objects.create(name = "comedy")
    Category.objects.create(name = "triller")
