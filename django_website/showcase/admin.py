from django.contrib import admin

from .models import Website, DjangoFeature

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)

class DjangoFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    

admin.site.register(Website, WebsiteAdmin)
admin.site.register(DjangoFeature, DjangoFeatureAdmin)
