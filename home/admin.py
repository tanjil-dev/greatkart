from django.contrib import admin
from .models import Images_Home

# Register your models here.
class Images_HomeAdmin(admin.ModelAdmin):
    list_display = ('Images_of_home',)

admin.site.register(Images_Home)
# admin.site.register(Images_HomeAdmin)