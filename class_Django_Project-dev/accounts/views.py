from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here
@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({
            "error":"Wrong method"
        })
    
    data = json.loads(request.body)
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    try:
        if not username or not email or not password:
           return JsonResponse({
            "error":"All Fields are Required"
            })
        if User.objects.filter(username=username).exists():
             return JsonResponse({
            "error":"User Already Exist"
            }) 
        
        if User.objects.filter(email=email).exists():
             return JsonResponse({
            "error":"User Already Exist"
            }) 
        user  = User(username=username,email=email,password=make_password(password))
        user.save()
        return JsonResponse({
            "message":"User has been created successfully",
            "status":True
            })
    
    except Exception as e:
      return JsonResponse({
          "error":e
      })

   
   
   

    return HttpResponse("<h1>Hello I am register</h1>")



# request methods 
# get put post patch delete 