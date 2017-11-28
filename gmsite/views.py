from django.shortcuts import render, render_to_response
from gmsite.models import Projects,Models,Services,News,Gallery,Image,ServicesSecond,ImageGallery,HomePhoto

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render



def index(request):
    content = {
        'News' : News.objects.all()[:3],
        'Photos' : HomePhoto.objects.all(),
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'home.html', content)

def services(request, pk):
    content = {
        'ServicesSecond' : ServicesSecond.objects.filter(service=pk),
        'Name' : Services.objects.filter(pk=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'services.html', content)

def service(request, pk):
    content = {
        'ServicesSecond' : ServicesSecond.objects.filter(service=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'service.html', content)

def model(request, pk):
    content = {
        'Projects' : Projects.objects.filter(model=pk).order_by("-id")[:3],
        'News' : Projects.objects.filter(model=pk)[:2],
        'Gallery' : Projects.objects.filter(model=pk).order_by("-id")[:3],
        'Services' : Services.objects.all(),
        'Name' : Models.objects.filter(pk=pk),
    }
    return render(request, 'model.html', content)

def projects(request):
    projectlist = Projects.objects.all().order_by("-id")
    paginator = Paginator(projectlist, 9)
    page = request.GET.get('page')
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project = paginator.page(paginator.num_pages)
    content = {
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'projects.html', content)

def project(request, pk):
    content = {
        'Models' : Models.objects.all(),
        'Project' : Projects.objects.filter(pk=pk),
        'Image' : Image.objects.filter(project=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'project.html', content)

def gallerys(request):
    projectlist = Projects.objects.all().order_by("-id")
    paginator = Paginator(projectlist, 9)
    page = request.GET.get('page')
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project = paginator.page(paginator.num_pages)
    content = {
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'gallerys.html', content)


def photogallery(request, pk):
    content = {
        'Gallery' : Gallery.objects.filter(id=pk),
        'Gallery_photo' : ImageGallery.objects.filter(gallery=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'photogallery.html', content)



def news(request):
    projectlist = Projects.objects.all().order_by("-id")
    paginator = Paginator(projectlist, 9)
    page = request.GET.get('page')
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project = paginator.page(paginator.num_pages)
    content = {
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'news.html', content)


def contact(request):

    return render(request, 'contact.html', content)
