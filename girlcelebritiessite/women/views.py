from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import RegistrationUserForm, AddPostForm
from .models import *
from .utils import DataMixin, menu


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Главная страница'}  # для статических тегов можно использовать

    # ниже для динамических и статических
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(context_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


#@login_required - как LoginRequiredMixin только для функций
def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    # success_lazy = reverse_lazy('home') - это надо использовать если нет absolute_url
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(context_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(context_def.items()))


def contact(request):
    return HttpResponse('Обратная связь.')


def login(request):
    return HttpResponse('Страница входа.')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].category),
                                            category_selected=context['posts'][0].category_id)
        return dict(list(context.items()) + list(context_def.items()))


class RegistrationUser(DataMixin, CreateView):
    form_class = RegistrationUserForm
    template_name = 'women/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(context_def.items()))



