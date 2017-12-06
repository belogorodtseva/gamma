from django.shortcuts import render, render_to_response
from gmsite.models import Question,Vacancy,NeedVacancy,Contact,Projects,Models,Services,News,Gallery,ImageBlock,ImageBlockNews,ServicesSecond,ImageGallery,ServicesSecondContent,ServicesSecondPriceTable,ServicesSecondPriceTableElement

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gmsite.forms import ContactForm



def index(request):
    content = {
        'Numbers' : Contact.objects.all(),
        'News' : News.objects.all()[:3],
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'home.html', content)

def services(request, pk):
    content = {
        'Numbers' : Contact.objects.all(),
        'ServicesSecond' : ServicesSecond.objects.filter(service=pk),
        'Name' : Services.objects.filter(pk=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'services.html', content)

def service(request, pk):
    pricetable = ServicesSecondPriceTable.objects.get(service=pk)
    content = {
        'Numbers' : Contact.objects.all(),
        'ServicesSecond' : ServicesSecond.objects.filter(pk=pk),
        'Content' : ServicesSecondContent.objects.filter(service=pk),
        'Price' : ServicesSecondPriceTable.objects.filter(service=pk),
        'PriceElements' : ServicesSecondPriceTableElement.objects.filter(service=pricetable.pk),
        'Gallery' : Gallery.objects.filter(service=pk)[:1],
        'Services' : Services.objects.all(),
    }
    return render(request, 'service.html', content)

def model(request, pk):
    content = {
        'Numbers' : Contact.objects.all(),
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
        'Numbers' : Contact.objects.all(),
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'projects.html', content)

def projectsmodel(request, pk):
    projectlist = Projects.objects.filter(model=pk).order_by("-id")
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
        'Numbers' : Contact.objects.all(),
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
        'Name' : Models.objects.filter(pk=pk),
    }
    return render(request, 'projectsmodel.html', content)

def project(request, pk):
    content = {
        'Numbers' : Contact.objects.all(),
        'Project' : Projects.objects.filter(pk=pk),
        'Image' : ImageBlock.objects.filter(project=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'project.html', content)

def gallery(request):
    projectlist = Gallery.objects.all().order_by("-id")
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
        'Numbers' : Contact.objects.all(),
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'gallery.html', content)

def galleryserv(request, pk):
    projectlist = Gallery.objects.filter(service=pk).order_by("-id")
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
        'Numbers' : Contact.objects.all(),
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
        'Name' : ServicesSecond.objects.filter(pk=pk),
    }
    return render(request, 'galleryserv.html', content)


def photogallery(request, pk):
    content = {
        'Numbers' : Contact.objects.all(),
        'Gallery' : Gallery.objects.filter(id=pk),
        'Photo' : ImageGallery.objects.filter(gallery=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'photogallery.html', content)



def news(request):
    projectlist = News.objects.all().order_by("-id")
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
        'Numbers' : Contact.objects.all(),
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'news.html', content)

def newsmodel(request, pk):
    projectlist = News.objects.filter(model=pk).order_by("-id")
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
        'Numbers' : Contact.objects.all(),
        'Projects' : project,
        'Models' : Models.objects.all(),
        'Services' : Services.objects.all(),
        'Name' : Models.objects.filter(pk=pk),
    }
    return render(request, 'newsmodel.html', content)

def article(request, pk):
    content = {
        'Numbers' : Contact.objects.all(),
        'Project' : News.objects.filter(pk=pk),
        'Image' : ImageBlockNews.objects.filter(news=pk),
        'Services' : Services.objects.all(),
    }
    return render(request, 'article.html', content)


def contact(request):
    content = {
        'Numbers' : Contact.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'contact.html', content)

def about(request):
    content = {
        'Numbers' : Contact.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'about.html', content)

def vacancy(request):
    content = {
        'Vacancy' : Vacancy.objects.all(),
        'Need' : NeedVacancy.objects.all(),
        'Numbers' : Contact.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'vacancy.html', content)

def askme(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print('yes')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = "Вопрос на сайте"
        message = form.cleaned_data.get('message')
        from_email = settings.EMAIL_HOST_USER
        contact_message= "NAME: \n%s \n\nMESSAGE: \n%s \n\n from %s"%(
                name,
                message,
                email)
        send_mail(subject,contact_message,from_email,['annbelogorodtseva@gmail.com'],fail_silently=False)
    content = {
        'form': form,
        'Questions' : Question.objects.all(),
        'Numbers' : Contact.objects.all(),
        'Services' : Services.objects.all(),
    }
    return render(request, 'askme.html', content)
