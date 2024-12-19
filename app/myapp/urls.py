
from django.urls import path
from myapp.views import first


urlpatterns=[
    path("",first,name="login")
]