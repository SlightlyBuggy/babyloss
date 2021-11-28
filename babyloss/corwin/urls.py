from django.urls import path

from . import views

app_name = 'corwin'
urlpatterns = [
    path('', views.index, name='index'),
    path('babyloss', views.babyloss, name='babyloss'),
    path('resources_expecting', views.resources_expecting, name='resources_expecting'),
    path('resources_loss', views.resources_loss, name='resources_loss'),
    path('resources_doulas', views.resources_doulas, name='resources_doulas'),
    path('resources_providers', views.resources_providers, name='resources_providers'),
    path('resources_loved', views.resources_loved, name='resources_loved'),
    path('resources_employers', views.resources_employers, name='resources_employers'),
    path('corwin_story', views.corwin_story, name='corwin_story'),
    path('about', views.about, name='about'),
]