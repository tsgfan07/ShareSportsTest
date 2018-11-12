from django.shortcuts import render
from UploadPage.models import Article
from django.http import HttpResponse
from UploadPage.choices import *
import geopy
from geopy.geocoders import Nominatim
from geopy import distance


def index(request):
    article_list=Article.objects.order_by('id')
    context = {'article_list': article_list,}
    #return HttpResponse('<h1>index status</h1>')
    return render(request, 'SearchPage/home.html', context)


def search(request):
    if request.method == 'GET': # this will be GET now
        search_name = request.GET.get('search') # do some research what it does
        geopy.geocoders.options.default_format_string = '%s Deutschland'
        geolocator = Nominatim(user_agent="gearshare2018")
        if request.GET.get('user_location')==None:
            user_location_city = geolocator.geocode("76131 Karlsruhe")
        else:
            user_location_city = geolocator.geocode(request.GET.get('user_location'))

        if True:
        #try:
            status = Article.objects.filter(title__icontains= search_name) # filter returns a list so you might consider skip except part
            context = {"article_list": status, "user_location": user_location_city}
            context=order_by_distance(context)
            return render(request, 'SearchPage/home.html', context)

        #except Exception as e:
            #return HttpResponse(e)
    if request.method == 'POST':  # this will be GET now
        tag_name = request.POST['search_select']  # do some research what it does
        try:
            t = 0
            string_s=""
            for i in Article._meta.get_field('category').choices:
                string_s =[string_s,i[1]]
                if tag_name == i[1]:
                    t = i[0]
            geopy.geocoders.options.default_format_string = '%s Deutschland'
            geolocator = Nominatim(user_agent="gearshare2018")
            if request.POST['user_location'] == None:
                user_location_city = geolocator.geocode("76131 Karlsruhe")
            else:
                user_location_city = geolocator.geocode(request.GET.get('user_location'))

            status = Article.objects.filter(category=t)  # filter returns a list so you might consider skip except part
            context = {"article_list": status, "user_location": user_location_city}
            context = order_by_distance(context)
             # filter returns a list so you might consider skip except part
            #return HttpResponse([tag_name,t, string_s])
            return render(request, 'SearchPage/home.html', context)
        except:
            return HttpResponse(t)
            #return render(request, "SearchPage/home.html", {})

def category_view(request):
    ### Get the categories without any parent.
    categories = [i[1] for i in Article._meta.get_field('category').choices]
    context = {'cat_list': categories}
    return render(request, 'SearchPage/cat_view.html', context=context)

def order_by_distance(context):

        user_location=context.get('user_location')
        user_location=geopy.point.Point.from_sequence([user_location.longitude, user_location.latitude,0])
        distance_list = [0.0 for x in range(len(context.get('article_list')))]
        article_list = context.get('article_list')
        counter = 0
        for article in article_list:
            x = distance.geodesic(geopy.point.Point.from_sequence([article.location_longitude, article.location_latitude,0]), user_location).km
            distance_list[counter] = x
            counter += 1
        z_list=zip(article_list, distance_list)
        context = {'article_list': sorted(z_list, key=lambda pair: pair[1]), 'user_location': user_location}
        return context


