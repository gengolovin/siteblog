from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/category_tpl.html')
def show_category():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag('blog/menu_category_tpl.html')
def show_menu_category():
    categories = Category.objects.all()
    return {"categories": categories}