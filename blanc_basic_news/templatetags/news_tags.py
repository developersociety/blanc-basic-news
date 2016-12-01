from django import template
from django.utils import timezone

from ..models import Category, Post

register = template.Library()


@register.assignment_tag
def get_news_categories():
    return Category.objects.all()


@register.assignment_tag
def get_news_months():
    return Post.objects.filter(published=True, date__lte=timezone.now()).dates('date_url', 'month')


@register.assignment_tag
def get_latest_news(count, category=None):
    post_list = Post.objects.select_related().filter(published=True, date__lte=timezone.now()).latest()

    # Optional filter by category
    if category is not None:
        post_list = post_list.filter(category__slug=category)

    return post_list[:count]
