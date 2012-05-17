from django.conf.urls import patterns, url
import feeds
import views


urlpatterns = patterns('',
    # RSS feed
    url(r'^feed/$',
        feeds.BasicNewsFeed(),
        name='feed'),
    url(r'^feed/(?P<slug>[-\w]+)/$',
        feeds.BasicNewsCategoryFeed(),
        name='category-feed'),

    # Pages
    url(r'^$',
        views.PostListView.as_view(),
        name='post-list'),
    url(r'^category/(?P<slug>[-\w]+)/$',
        views.PostListCategoryView.as_view(),
        name='post-list-category'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.PostListMonthView.as_view(),
        name='post-list-month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.PostDetailView.as_view(),
        name='post-detail'),
)
