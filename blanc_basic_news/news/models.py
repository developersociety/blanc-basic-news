from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blanc_basic_news:post-list-category', (), {
            'slug': self.slug,
        })


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    image = models.ImageField(
            upload_to='news/image/%Y/%m',
            height_field='image_height',
            width_field='image_width',
            blank=True)
    image_height = models.PositiveIntegerField(null=True, editable=False)
    image_width = models.PositiveIntegerField(null=True, editable=False)
    content = models.TextField()
    published = models.BooleanField(
            default=True,
            db_index=True,
            help_text='Post will be hidden unless this option is selected')

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blanc_basic_news:post-detail', (), {
            'year': self.date.year,
            'month': str(self.date.month).zfill(2),
            'day': str(self.date.day).zfill(2),
            'slug': self.slug,
        })
