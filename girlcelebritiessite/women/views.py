from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import *
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


class WomenHome(ListView):
    model = Women



# def index(request):
#     posts = Women.objects.all()
#
#     context = {'posts': posts,
#                'menu': menu,
#                'title': 'Главная страница',
#                'category_selected': 0
#                }
#     return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Добавление статьи'
    }
    return render(request, 'women/add_page.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'category_selected': post.category,
    }
    return render(request, 'women/post.html', context=context)


def contact(request):
    return HttpResponse('Обратная связь.')


def login(request):
    return HttpResponse('Страница входа.')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_category(request, category_slug):
    posts = Women.objects.filter(category__slug=category_slug)
    category = Category.objects.get(slug=category_slug)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               'category_selected': category.slug,
               }
    return render(request, 'women/index.html', context=context)
