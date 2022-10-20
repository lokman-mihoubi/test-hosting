from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .filters import Carfilter





def index(request):
    car_list= Car.objects.all()
    myfilter = Carfilter(request.GET,queryset=car_list)
    car_list = myfilter.qs
    paginator = Paginator(car_list, 1)
    page = request.GET.get('page')
    car_list = paginator.get_page(page)
    return render(request,'index.html',{'car_list':car_list,'myfilter': myfilter})
def car_detail(request,slug):
    car_detail=get_object_or_404(Car,SLug=slug)
    return render(request,'car_detail.html',{'car_detail':car_detail})



# Create your views here.
