from django.urls import path
from . import views

urlpatterns = [
    path("blogs/",views.blogs,name="blogs")
]

#  myproject.com/app1/blogs