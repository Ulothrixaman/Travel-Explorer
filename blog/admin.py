from django.contrib import admin
from .models import Category, Post, Gallery, Packages, Services


# Register your models here.

# for configuration of Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_pot', 'title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    class Media:
        js = ('js/style.js',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('gal_img',)
    list_per_page = 10


class PackagesAdmin(admin.ModelAdmin):
    list_display = ('pac_img', 'title', 'description', 'url', 'add_date')
    search_fields = ('url',)
    list_per_page = 10


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    search_fields = ('url', )
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(Services, ServicesAdmin)
