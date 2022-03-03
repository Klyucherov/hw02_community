from django.urls import path
from .views import index, group_posts
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
