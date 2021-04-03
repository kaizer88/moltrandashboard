from django.urls import path
from .views import HelloApiView


urlpatterns = [

    path('getweather', HelloApiView.as_view(), name='myweather'),

]
