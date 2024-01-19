from django.contrib import admin
from .models import Gallery, Packages, Services, Trips


# Register your models here.


# class Media:
#     js = ('js/style.js',)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('gal_img',)
    list_per_page = 10


class PackagesAdmin(admin.ModelAdmin):
    list_display = ('pac_img', 'title', 'description', 'url', 'add_date')
    search_fields = ('url',)
    list_per_page = 10


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('url',)
    list_per_page = 10


class TripAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Packages, PackagesAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Trips, TripAdmin)
