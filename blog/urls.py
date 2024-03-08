from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"), #root/blog
    path("front/", views.front, name="front"),
    path("business/", views.business, name="business"),
    
    path("home/", views.home, name="homepage"), #root/blog/home #views.attribute must match def attribute in views.py
    path("about/", views.about, name="about"), #no html yet, no view
    path("login/", views.login_page, name="login"), #no html yet, no view
    path("logout/", views.logout_request, name="logout"),
    path("archive/", views.archive, name="archive"),
    path("adarchive/", views.adarchive, name="adarchive"), #no html yet, no view

    path("<int:pk>/", views.postview, name= "postview"), #root/blog/pk
    path("<int:pk>/comments", views.commentview, name= "comments"),
    # remove comment url, also needs view
    # maybe? view all removed comments page, also needs view
    
    path("<int:pk>/publish/", views.publish_post, name= "publish"),
    path("<int:pk>/unpublish/", views.unpublish_post, name= "unpublish"),
    
    path("creatorview/", views.creatorview, name="creator"),
    path("<int:pk>/editview/", views.editview, name= "editview"), 
    path("<int:pk>/refuseview/", views.refuseview, name="refuse"),

    path("galleries/", views.galleries, name="galleries"), #no html, no view, no gallery model
    path("galleries/<int:pk>/", views.galleryone, name="gallery"), #no html, no view, no gallery model
    
    path("<int:pk>/thermos/", views.thermos, name="thermos"), # experimenting with root/folder/folder
    path("taglist/<int:tag_id>/", views.taglist, name="taglist"), # initially with tag_id, later switch to tag_name
    
    
]

