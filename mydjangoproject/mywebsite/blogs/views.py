#i am write
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

blog_names = {
    "python-intro": "<h1>Python Post</h1>",
    "django-basic" :"<h1>Django Basic blog posts</h1>",
    "python-oops":"<h1>oop with python</h1>",
    "regex" : "<h1>Regular Expression in python</h1>"
}


# Create your views here.
def home_page(request):
    res_data = render_to_string("blogs/index.html")
    return HttpResponse(res_data)
   # return HttpResponse("<h1>Home page of our blogs</h1>")

def blogposts(request):
    list_items=""
    blog_list=list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog-post",args=[b])
        list_items +=f'<li><a href = "{blog_path}">{b.capitalize()}</a></li>'


    res_data = f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)
#---------------- --------------------------------------------------
    # res_data="""
    # <ul> 
    #     <li><a href = "/allpost/python-intro">Python Intro</a></li>
    #     <li><a href = "/allpost/django-basic">Django Basic</a></li>
    #     <li><a href = "/allpost/python-oops">Python OOOP</a></li>
    #     <li><a href = "/allpost/regex">Reguler Expression</a></li>
    # </ul>
    # """
    # return HttpResponse(f"<h1>All Blog posts! </h1> \n  {res_data}")
    # return HttpResponse(res_data)
#---------------------------------------------

# def python_intro(request):
#     return HttpResponse("<h1>Python post<h1>")

# def django_basic(request):
#     return HttpResponse("<h1>Django basic blog post<h1>")

# def python_oops(request):
#     return HttpResponse("<h1>oop with python<h1>")

#def blog_post(request,blog):# dynamic path segment for
    # if blog == "python-intro":
    #     res ="<h1>Python Post</h1>"
    # elif blog == "django-basic":
    #     res = "<h1>Django Basic blog posts</h1>"
    # elif blog == "python-oops":
    #     res = "<h1>oop with python</h1>"
    # else:
    #   return HttpResponseNotFound("<h1>Blog not found</h1>")
    # return HttpResponse(res)


def blog_post(request,blog):  
    try:  
      res = blog_names[blog]
    except Exception:
        return HttpResponseNotFound("<h1>Blog not found</h1>")
    else:
        return HttpResponse(res)



   #  path converter

# def blog_post_by_number(request,name):
#     return HttpResponse(f"Your blog is : {name}") # path converter

