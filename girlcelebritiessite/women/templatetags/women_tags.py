from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='get_categories') # можно указать любое имя ииспользовать его в шаблонах
def get_categories(filter=None):
    if filter:
        return Category.objects.filter(slug=filter)
    return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if sort:
        categories = Category.objects.order_by(sort)
        return {'categories': categories, 'category_selected': category_selected}
    categories = Category.objects.all()
    return {'categories': categories, 'category_selected': category_selected}


