from django.shortcuts import render, redirect, HttpResponse
from rest_framework import viewsets

from .serializers import SerializeShop, SerializeUser
from .models import Shop, User
import math


# REST API CLASS
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all().order_by('name')
    serializer_class = SerializeShop

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = SerializeUser


def view(request):
    if request.method == 'GET':
        details = Shop.objects.all()
        return render(request, 'mainapp/view.html', {"details": details})
    else:
        if request.POST['action'] == 'Update':
            if(Shop.objects.filter(name=request.POST['name']).update(
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
                address=request.POST['address']
            )):
                return HttpResponse("<script>alert('successfully updated');location.href = '/'</script>")
            else:
                return HttpResponse("<script>alert('Something went wrong');location.href = '/'</script>")

        elif request.POST['action'] == 'Delete':
            if(Shop.objects.filter(name=request.POST['name']).delete()[0]):
                return HttpResponse("<script>alert('successfully deleted');location.href = '/'</script>")
            else:
                return HttpResponse("<script>alert('Something went wrong');location.href = '/'</script>")


def add(request):
    if request.method == 'GET':
        print("inside add if")

        return render(request, 'mainapp/add.html')
    else:
        # print("inside add else")
        s = Shop(name=request.POST['name'].replace(" ", "_"),
                           latitude=request.POST['latitude'],
                           longitude=request.POST['longitude'],
                           address=request.POST['address'])
        
        s.save()
        return HttpResponse("<script>alert('success');location.href = '/'</script>")
    
def add_user(request):
    if request.method == 'GET':
        return render(request, 'mainapp/adduser.html')
    else:
        print('request parameters')
        print(request.POST['latitude'], request.POST['distance'], request.POST.get('longitude'))
        s = User(name=request.POST['name'].replace(" ", "_"),
                           latitude=request.POST['latitude'],
                           longitude=request.POST['longitude'],
                           distance=request.POST['distance'])
        entries = shops_within_distance(request)
        # return HttpResponse("<script>alert('success');location.href = '/'</script>")
        return  render(request, 'mainapp/shops_within_distance.html', {'entries':entries, 'distance': request.POST['distance']})


# from django.shortcuts import render
# from django.db.models.functions import Acos, Cos, Radians, Sin
# from django.db.models import FloatField, Value
# from django.contrib.gis.db.models.functions import Distance
# from .models import Shop

def shops_within_distance(request):
    # if request.method == 'POST':
    lat = float(request.POST['latitude'])
    lon = float(request.POST['longitude'])
    radius = float(request.POST['distance'])
    entries = []
    Shops = Shop.objects.all()
    # for x in Shops:
    #     print('for statement')
    #     print(x)
    for entry in Shops:
        lat2 = entry.latitude
        lon2 = entry.longitude
        dlat = math.radians(lat2 - lat)
        dlon = math.radians(lon2 - lon)
        a = math.sin(dlat/2) * math.sin(dlat/2) + \
            math.cos(math.radians(lat)) * math.cos(math.radians(lat2)) * \
            math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = 6371 * c  # km
        if distance <= radius:
            entries.append(entry)
        return entries

   

