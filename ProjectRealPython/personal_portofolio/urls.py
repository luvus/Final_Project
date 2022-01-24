from django.contrib import admin
from django.urls import path, include , re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
 

]
