# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
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


class AbstractPost(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=100, unique_for_date='date_url')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    date_url = models.DateField(
        'Publish on',
        default=timezone.now
    )
    image = models.ImageField(
        upload_to='news/image/%Y/%m',
        height_field='image_height',
        width_field='image_width',
        blank=True
    )
    image_height = models.PositiveIntegerField(null=True, editable=False)
    image_width = models.PositiveIntegerField(null=True, editable=False)
    teaser = models.TextField(blank=True)
    content = models.TextField()
    published = models.BooleanField(
        default=True,
        db_index=True,
        help_text='Post will be hidden unless this option is selected'
    )
    url = models.URLField(blank=True)

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)
        abstract = True

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return reverse('blanc_basic_news:post-detail', kwargs={
                'year': self.date_url.year,
                'month': str(self.date_url.month).zfill(2),
                'day': str(self.date_url.day).zfill(2),
                'slug': self.slug,
            })

    def save(self, *args, **kwargs):
        super(AbstractPost, self).save(*args, **kwargs)


class Post(AbstractPost):
    class Meta(AbstractPost.Meta):
        swappable = 'NEWS_POST_MODEL'
