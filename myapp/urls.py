from django.urls import path
from myapp.views import get_func


urlpatterns = [
    path('', get_func)
]