__author__ = 'gray'

from django import template
from apprango.models import Category

register = template.Library()

@register.inclusion_tag('apprango/categories.html')
def get_cat_list(cat=None):
    return {'categs': Category.objects.all(), 'active_cat': cat}