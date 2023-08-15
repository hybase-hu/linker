from django.contrib import admin

from web_pages.models import WebRequest, WebPage

# Register your models here.
admin.site.register(WebRequest)
admin.site.register(WebPage)
