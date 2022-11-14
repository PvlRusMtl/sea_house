from django.shortcuts import render, get_object_or_404
from houses.models import House

def houses_list(request):
    houses = House.objects.all()
    for house in houses:
        print(house.name, house.price)
    return render(request, "houses/houses_list.html", {'houses': houses})

def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    return render(request, "houses/houses_detail.html", {'house': house})