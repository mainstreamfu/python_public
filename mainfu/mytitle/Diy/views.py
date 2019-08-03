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

#登录页面
def logIn(request):

    return render(request,'login.html')

def get_valid_img(request):
    import random
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    from PIL import Image
    from io import BytesIO
    from PIL import ImageDraw, ImageFont
    f = BytesIO()
    image = Image.new(mode="RGB", size=(120, 80), color=get_random_color())
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Diy/static/fonts/kumo.ttf", size=36)

    temp = []
    for i in range(5):
        random_char = random.choice(
            [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        draw.text((i * 24, 26), random_char, get_random_color(), font=font)
        temp.append(random_char)
    width = 120
    height = 80
    image.save(f, "png")
    data = f.getvalue()
    request.session["random_code_str"]="".join(temp)
    return HttpResponse(data)
