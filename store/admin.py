from django.contrib import admin

from . import models
admin.site.register(models.Store)
admin.site.register(models.Category)
admin.site.register(models.Tag)
