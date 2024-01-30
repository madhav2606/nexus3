from django.urls import path

from . import views

urlpatterns = [
    path("about", views.about, name ="about"),
    path("services", views.services, name ="services"),
    path("contactus", views.contactus, name ="contactus"),
    # path("index", views.home, name ="home"),


]