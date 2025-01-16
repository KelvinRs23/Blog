from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import ImageFilter
from .forms import PostForm

# Create your views here.

def kategori(request):
    return render(request, 'account/kategori.html'),



def home(request):
    posts = Comment.objects.all()
    post_form = PostForm()
    pics=Image.objects.all()

    context = {
        'pics':pics,
        'post_form':post_form,
        'page_title':'All Comments',
        'posts':posts,
        }

    if request.method == 'POST':
        Comment.objects.create(
            Nama = request.POST['Nama'],
            Komentar = request.POST['Komentar'],
            )

    pics = ImageFilter(
        request.GET,
        queryset = Image.objects.all()
    )
    
    context['pics'] = pics

    return render(request, 'account/dashboard.html', context=context)

def posting(request):
    return render(request, 'account/posting.html')

def horror(request):
    return render(request, 'account/horror.html')
def comedy(request):
    return render(request, 'account/comedy.html')
def romance(request):
    return render(request, 'account/romance.html')

def upload(request):
    pics=Image.objects.all()

    context = {'pics':pics}

    pics = ImageFilter(
        request.GET,
        queryset = Image.objects.all()
    )
    
    context['pics'] = pics

    return render(request, 'account/readmore.html', context=context)

def button(request):
    pics=Image.objects.all()

    context = {'pics':pics}

    pics = ImageFilter(
        request.GET,
        queryset = Image.objects.all()
    )
    
    context['pics'] = pics

    return render(request, 'account/button.html', context=context)

def about(request):
    pics=Image.objects.all()

    context = {'pics':pics}

    pics = ImageFilter(
        request.GET,
        queryset = Image.objects.all()
    )
    
    context['pics'] = pics

    return render(request, 'account/about.html', context=context)

def contact(request):
    pics=Image.objects.all()

    context = {'pics':pics}

    pics = ImageFilter(
        request.GET,
        queryset = Image.objects.all()
    )
    
    context['pics'] = pics

    return render(request, 'account/contact.html', context=context)