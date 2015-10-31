from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Category, Post


class BasicNewsFeed(Feed):
    title = getattr(settings, 'NEWS_TITLE', 'News')
    link = reverse_lazy('blanc_basic_news:post-list')

    def items(self):
        feed_limit = getattr(settings, 'NEWS_FEED_LIMIT', 10)
        return Post.objects.filter(published=True, date__lte=timezone.now())[:feed_limit]

    def item_description(self, obj):
        return obj.content

    def item_pubdate(self, obj):
        return obj.date

    def item_guid(self, obj):
        return '%s:news:%d' % (Site.objects.get_current().domain, obj.pk)


class BasicNewsCategoryFeed(BasicNewsFeed):
    def get_object(self, request, slug):
        return get_object_or_404(Category, slug=slug)

    def title(self, obj):
        return '%s - %s' % (getattr(settings, 'NEWS_TITLE', 'News'), obj.title)

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        feed_limit = getattr(settings, 'NEWS_FEED_LIMIT', 10)
        return Post.objects.filter(
            published=True, date__lte=timezone.now(), category=obj)[:feed_limit]
