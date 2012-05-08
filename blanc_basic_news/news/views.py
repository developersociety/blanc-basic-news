from django.views.generic import ListView, DateDetailView
from django.utils import timezone
from django.conf import settings
from .models import Post


class PostListView(ListView):
    paginate_by = getattr(settings, 'NEWS_PER_PAGE', 10)

    def get_queryset(self):
        return Post.objects.filter(published=True, date__lte=timezone.now())


class PostDetailView(DateDetailView):
    queryset = Post.objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'
