from django.shortcuts import render
from django.http import HttpResponse
from .models import Sport, Area, Equipment
from django.template import loader


def index(request):
    return HttpResponse("Hello, You're at the Gym index.")


# noinspection PyInterpreter,PyInterpreter
def my_view(request):
    sports = Sport.objects.all()
    area_count = 1
    equipment_count = 1
    for sport in sports:
        area_count = max(len(sport.area_set.all()), area_count)
        equipment_count = max(len(sport.equipment_set.all()), equipment_count)
    template = loader.get_template('Gym/my_view.html')
    context = {
        'sports': sports,
        'area_count': area_count,
        'equipment_count': equipment_count
    }
    #output = ", ".join([obj.sport_name for obj in sports])
    return HttpResponse(template.render(context, request))

