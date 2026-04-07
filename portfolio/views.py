from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Project


@never_cache
def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})
