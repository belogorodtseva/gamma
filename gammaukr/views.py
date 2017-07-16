from django.shortcuts import render, render_to_response
from gammaukr.models import Projects,Projects_steps,Models,Services,News,News_steps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404



def index(request):
    content = {
        'Projects' : Projects.objects.all(),
        'Models' : Models.objects.all(),
    }
    return render(request, 'gammaukr/home.html', content)

def projects(request):
    content = {
        'Projects' : Projects.objects.all(),
        'Services' : Services.objects.all(),
        'Models' : Models.objects.all(),
    }
    return render(request, 'gammaukr/projects.html', content)

def projectservices(request, pk):
    content = {
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
        'Projects' : Projects.objects.all().filter(model=pk),
        'Car' : Services.objects.all().filter(pk=pk),
    }
    return render(request, 'gammaukr/projectservices.html', content)

def project(request, pk):
    content = {
        'Project' : Projects.objects.filter(pk=pk),
        'Detail' : Projects_steps.objects.filter(project=pk),
    }
    return render(request, 'gammaukr/project.html', content)

def projectcar(request, pk):
    content = {
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
        'Projects' : Projects.objects.all().filter(model=pk),
        'Car' : Models.objects.all().filter(pk=pk),
    }
    return render(request, 'gammaukr/projectcar.html', content)

def services(request):
    content = {
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'gammaukr/services.html', content)

def news(request):
    content = {
        'Models' : Models.objects.all(),
        'News' : News.objects.all(),
    }
    return render(request, 'gammaukr/news.html', content)
