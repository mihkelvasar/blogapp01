from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"), #root/blog
    path("home/", views.home, name="homepage"), #root/blog/home #views.attribute must match def attribute in views.py
    path("<int:pk>/", views.postview, name= "postview"), #root/blog/pk
    path("archive/", views.archive, name="archive"),
    path("<int:pk>/editview/", views.editview, name= "editview"), 
    path("<int:pk>/thermos/", views.thermos, name="thermos"), # experimenting with root/folder/folder
    path("<int:pk>/refuseview/", views.refuseview, name="refuse"),
    path("home/creatorview/", views.creatorview, name="creator"),
]

