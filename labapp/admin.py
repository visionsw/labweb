from django.contrib import admin
from .models import Area, Mehtods, Link

# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['pk', "acname", "aename", "methodnum", "adescription", "ainfolink"]
    list_filter = ["acname", "aename", "methodnum"]
    search_fields = ["acname", "aename", "methodnum"]
    list_per_page = 10

    fields = ["acname", "aename", "methodnum", "adescription", "ainfolink"]


@admin.register(Mehtods)
class MethodsAdmin(admin.ModelAdmin):
    list_display = ["pk", "mcname", "mename", "mtype", "mdescription", "minfolink", "myear", "mpersons", "mhot"]
    list_filter = ["mcname", "mename", "mtype", "myear", "mpersons", "mhot"]
    search_fields = ["mcname", "mename", "mtype", "myear", "mpersons", "mhot"]
    list_per_page = 10

    fields = ["mcname", "mename", "mtype", "mdescription", "minfolink", "myear", "mpersons", "mhot"]


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["pk", "url", "source", "method", "linkhot"]
    list_filter = ["url", "source", "method", "linkhot"]
    search_fields = [ "url", "source", "method", "linkhot"]
    list_per_page = 10

    fields = ["url", "source", "method", "linkhot"]