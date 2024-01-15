import datetime

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Category, Gallery, Packages, Services


# Create your views here.
def home(request):
    # load all the posts from db
    posts = Post.objects.all()[:11]

    cats = Category.objects.all()

    gals = Gallery.objects.all()

    data = {
        'posts': posts,
        'cats': cats,
        'gals': gals
    }
    return render(request, 'home.html', data)


def book(request):
    try:
        dest = request.GET.get('destination')
        num = int(request.GET.get('num'))
        departure = (request.GET.get('departure'))
        arrival = request.GET.get('arrival')
        fname = request.GET.get('fname')
        lname = request.GET.get('lname')
        age = int(request.GET.get('age'))
        gender = request.GET.get('gender')
        print(dest)
        print(num)
        print(departure)
        print(arrival)
        print(fname)
        print(lname)
        print(age)
        print(gender)
    except:
        pass
    return render(request, 'book.html', {})


def services(request):
    return render(request, 'services.html', {})


def about(request):
    return render(request, 'about.html', {})


def packages(request):
    # load all the posts from db
    packs = Packages.objects.all()
    data = {
        'packs': packs,
    }
    return render(request, 'packages.html', data)


def package(request, url):
    packs = Packages.objects.get(url=url)
    print(packs)
    return render(request, 'package.html', {'packs': packs})
