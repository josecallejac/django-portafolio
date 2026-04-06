from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Project


@cache_page(60 * 10)
def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})
