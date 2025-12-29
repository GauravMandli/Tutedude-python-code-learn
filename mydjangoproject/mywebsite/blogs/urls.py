# i m write
from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_page,name="homePage") ,
    path("allpost/",views.blogposts,name="blogposts"),
    # path("allpost/python-intro/",views.python_intro,name="PythonIntro"),
    # path("allpost/django-basics/",views.django_basic,name="DjangoBAsic"),
    # path("allpost/python-oops/",views.python_oops,name="PythonOOP"),
    # path("allpost/<str:blog>/",views.blog_post),#dynamic path sagment
    # path("allpost/<str:name>/",views.blog_post_by_number),#path converter 
    path("allpost/<slug:blog>/",views.blog_post,name="blog-post")#slug path converter 

]