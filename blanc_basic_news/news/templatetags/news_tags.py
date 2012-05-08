from django import template
from blanc_basic_news.news.models import Category, Post

register = template.Library()


@register.assignment_tag
def get_news_categories():
    return Category.objects.all()


@register.assignment_tag
def get_news_months():
    return Post.objects.dates('date', 'month')
