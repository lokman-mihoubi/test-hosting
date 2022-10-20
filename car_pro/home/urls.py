from django.urls import path
from . import views
app_name = "home"
urlpatterns = [

    path('', views.index,name='index'),
    path('<slug:slug>',views.car_detail,name='car_detail'),

]
