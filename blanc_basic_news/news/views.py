from django.views.generic import ArchiveIndexView, MonthArchiveView, DateDetailView
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Category
from . import get_post_model


class PostListView(ArchiveIndexView):
    queryset = get_post_model().objects.select_related().filter(published=True)
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
    queryset = get_post_model().objects.select_related().filter(published=True)
    month_format = '%m'
    date_field = 'date_url'


class PostDetailView(DateDetailView):
    queryset = get_post_model().objects.select_related().filter(published=True)
    month_format = '%m'
    date_field = 'date_url'
