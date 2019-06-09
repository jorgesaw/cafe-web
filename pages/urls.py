from django.urls import path
from . import views

urlpatterns = [ 
    path('<int:pk>/<slug:page_slug>/', views.page, name="page"), 
]