from django.contrib import admin

from .models import AUV, AUVData


@admin.register(AUV)
class AUVAdmin(admin.ModelAdmin):
    pass


@admin.register(AUVData)
class AUVDataAdmin(admin.ModelAdmin):
    pass

