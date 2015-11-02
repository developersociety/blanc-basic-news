from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import ArchiveIndexView, DateDetailView, MonthArchiveView

from .models import Category, Post


class PostListView(ArchiveIndexView):
    queryset = Post.objects.select_related().filter(published=True)
    date_field = 'date'
    paginate_by = getattr(settings, 'NEWS_PER_PAGE', 10)
    template_name_suffix = '_list'
    context_object_name = 'object_list'


class PostListCategoryView(PostListView):
    template_name_suffix = '_list_category'

    def get_queryset(self):
        qs = super(PostListCategoryView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostListCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class PostListMonthView(MonthArchiveView):
    queryset = Post.objects.select_related().filter(published=True)
    month_format = '%m'
    date_field = 'date_url'


class PostDetailView(DateDetailView):
    queryset = Post.objects.select_related().filter(published=True)
    month_format = '%m'
    date_field = 'date_url'
