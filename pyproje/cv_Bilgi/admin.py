from django.contrib import admin
from .models import Bilgi

# Register your models here.

class BilgiAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Surname','slug']
    list_display_links = ['Surname']
    list_filter = ['Surname']
    search_fields = ['Name', 'content','Surname']
    list_editable = ['Name']

    class Meta:
        model = Bilgi

admin.site.register(Bilgi,BilgiAdmin)