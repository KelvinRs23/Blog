from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import ImageFilter
from .forms import PostForm, FilmForm, CategoryForm


# Create your views here.

def kategori(request):
    return render(request, 'account/kategori.html'),


def category(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'account/navbar.html', context=context)



def home(request):
    posts = Comment.objects.all()
    post_form = PostForm()
    pics=Image.objects.all()
    films = Film.objects.all()
    category = Category.objects.all()

    category_filter = request.GET.get('kategori', None)

    if category_filter:
        films = Film.objects.filter(kategori__nama=category_filter)
    else:
        films = Film.objects.all()

    context = {
        'pics':pics,
        'post_form':post_form,
        'page_title':'All Comments',
        'posts':posts,
        'films': films,
        'category': category,
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

def film_list(request):
    films = Film.objects.all()
    return render(request, 'account/film_list.html', {'films': films})
def create_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'account/film.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'account/category_list.html', {'categories': categories})
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'account/category.html', {'form': form})

