from django.urls import path, include
from myurls import views
urlpatterns = [
    path('show/', views.show, name='show'),
    path('test/', views.test, name='test'),
]