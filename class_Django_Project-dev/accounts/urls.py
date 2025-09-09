
from django.contrib import admin
from django.urls import path
from .views import register
from django.http import JsonResponse, HttpResponse

def homePage(request):
    return HttpResponse('<h1>I am home page</h1>')




urlpatterns = [
   path('', homePage ),
   path('register/', register )

]

# http://localhost:8000/accounts/dashboard

