from django.urls import path

from . import views

app_name = 'corwin'
urlpatterns = [
    path('', views.index, name='index'),
    # path('dream', views.dream, name='dream'),
]