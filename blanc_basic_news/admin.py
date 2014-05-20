from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Post)
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
