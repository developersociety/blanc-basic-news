from django import template
from django.utils import timezone
from blanc_basic_news.news.models import Category, Post

register = template.Library()


@register.assignment_tag
def get_news_categories():
    return Category.objects.all()


@register.assignment_tag
def get_news_months():
    return Post.objects.dates('date', 'month')


@register.assignment_tag
def get_latest_news(count):
        return Post.objects.select_related().filter(
                published=True, date__lte=timezone.now())[:count]
