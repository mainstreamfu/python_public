from django.shortcuts import render,redirect,HttpResponse
from .models import *
from Diy.forms import *

# Create your views here.

#注册页面

def reg(request):
    avatar_obj = request.FILES.get("avatars")
    # print(type(avatar_obj))
    if request.is_ajax():
        register_form = RegisterForm(request.POST)
        reg_response = {"user":None,"error_msg":None}
        if register_form.is_valid():
            user = register_form.cleaned_data.get("user")
            pwd = register_form.cleaned_data.get("pwd")
            email = register_form.cleaned_data.get("email")
            avatar_obj = request.FILES.get("avatars")
            user_obj = UserInfo.objects.create_user(username=user,password=pwd,email=email,avatar=avatar_obj)
            reg_response["user"] = user_obj.username
        else:
             reg_response["error_msg"] = register_form.errors
        import json
        return HttpResponse(json.dumps(reg_response))
    register_form=RegisterForm()
    return render(request,'register.html',locals())

def logIn(request):


    return render(request,'login.html')