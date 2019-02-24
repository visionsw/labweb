from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import *
# Create your views here.


def index(request):

    class Tarea:
        methods = Mehtods()

        def __init__(self, name):
            self.name = name

    areas = Area.objects.all()
    areas_objects_list = list()

    for area in areas:
        methods_list = Mehtods.objects.filter(mtype=area)
        area_object = Tarea(area.acname)
        area_object.methods = [method for method in methods_list]
        areas_objects_list.append(area_object)

    return render(request, 'index.html', {"areas": areas_objects_list})


def search(request):
    mcname = request.POST["keyword"]
    methods = Mehtods.objects.filter(Q(mcname__icontains=mcname) | Q(mdescription__icontains=mcname) |
                                     Q(mename__icontains=mcname))
    areas = []
    for method in methods:
        areas.append(method.mtype)
    area_methods = []
    for area in areas:
        area_methods += Mehtods.objects.filter(mtype=area)
    area_methods = set(area_methods)
    return render(request, "searchresults.html", {"methods": methods, "area_methods": area_methods})


def method_show(request, mcname):

    class Tarea:
        methods = Mehtods()

        def __init__(self, name):
            self.name = name

    areas = Area.objects.all()
    areas_objects_list = list()

    for area in areas:
        methods_list = Mehtods.objects.filter(mtype=area)
        area_object = Tarea(area.acname)
        area_object.methods = [method for method in methods_list]
        areas_objects_list.append(area_object)

    return render(request, "method.html", {"c": mcname, "areas": areas_objects_list})

