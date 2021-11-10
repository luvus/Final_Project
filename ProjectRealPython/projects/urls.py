from django.urls import path
from . import views


urlpatterns = [

    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('create_new_project/',views.ProjectCreateView.as_view(), name='create-new-project'),
]