from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("defect-metrics", views.show_defects, name="defect metrics")
]
