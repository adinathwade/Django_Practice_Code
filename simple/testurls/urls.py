from django.urls import path, include
from testurls import views
urlpatterns = [
    path('', views.display, {'test' : 'ok' }, name='display'),
]