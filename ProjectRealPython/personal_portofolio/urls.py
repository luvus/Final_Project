from django.contrib import admin
from django.urls import path, include , re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path("",TemplateView.as_view(template_name="home_index.html")),
    path("",include("home.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
 

]

# from django.contrib import admin
# from django.urls import path, include , re_path
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path("/", include("users.urls")),
#     path("admin/", admin.site.urls),
#     path("projects/", include("projects.urls")),
#     path("blog/", include("blog.urls")),
 

# ]
