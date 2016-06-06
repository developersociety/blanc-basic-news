# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.sites.models import Site
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
       'slug': ('title',)
    }


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'date', 'image', 'teaser', 'content')
        }),
        ('Advanced options', {
            'fields': ('slug', 'published')
        }),
    )
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'category', 'published')
    list_editable = ('published',)
    list_filter = ('published', 'date', 'category')
    prepopulated_fields = {
       'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
