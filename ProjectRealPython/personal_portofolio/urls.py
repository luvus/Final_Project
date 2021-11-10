from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
 

]
