from django.urls import path
from . import views # from current folder, import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello) # route, reference to function
]