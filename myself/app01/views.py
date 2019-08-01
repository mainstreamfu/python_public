from django.shortcuts import render,redirect,HttpResponse
from . import models
from django.urls import reverse
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def reg(request):
    User.objects.create_user(username="yanlin",password="yanlin1234")
    return redirect("/login/")


#登录页面
def log_in(request):
    if request.is_ajax():
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        valid_code = request.POST.get("valid_code")
        code_str = request.session.get("random_code_str")
        login_response = {"user": None, "error_msg": ""}
        if valid_code.upper() == code_str.upper():

            user = auth.authenticate(username=user,password=pwd)
            if user:
                login_response["user"] = user.username
                auth.login(request,user)
            else:
                login_response["error_msg"] = "用户名或密码错误"
        else:
            login_response["error_msg"]="验证码错误"
        import json
        return HttpResponse(json.dumps(login_response))
    return render(request,"login.html")

def index(request):
    user = request.user
    # if not user.is_authenticated:
    #     return redirect("/login/")
    return render(request, "index.html", locals())

def log_out(request):
    auth.logout(request)
    return redirect("/login/")


#验证码
def get_valid_img(request):
    import random
    def get_random_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    from io import BytesIO
    #引入PIL时候要先安装pillow
    from PIL import Image,ImageDraw,ImageFont

    f = BytesIO()

    image = Image.new(mode="RGB", size=(60, 35), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("static/font/kumo.ttf",size=24)
    draw.text((0, 0), '', get_random_color(), font=font)
    temp = []
    for i in range(4):
        random_char = random.choice(
            [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        draw.text((i * 14, 7), random_char, get_random_color(), font=font)
        temp.append(random_char)
    width =60
    height = 40
    for i in range(40):
        draw.point((random.randint(0,width),random.randint(0,height)),fill=get_random_color())

    for i in range(2):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw.line((x1,y1,x2,y2),fill=get_random_color())
    for i in range(20):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    image.save(f,'png')
    data = f.getvalue()

    request.session["random_code_str"] = "".join(temp)

    return HttpResponse(data)



# 班级页面
def class_list(request):
    data = []
    class_list = models.Class.objects.all()

    for i in class_list:
        data.append(i)

    page_num = request.GET.get("page")
    path = request.path_info
    from tools.mypage import MyPage
    page = MyPage(page_num, len(data), path)
    page_html = page.page_html()
    return render(request,"class_list.html",{"class_list": data[page.start:page.end], "page_html": page_html})

def delete_class(request):
    class_id = request.GET.get("class_id")
    models.Class.objects.filter(id=class_id).delete()
    return  redirect(reverse('class_list'))

def add_class(request):
    if request.method == "POST":
        cname = request.POST.get("cname")
        models.Class.objects.create(cname=cname)
        return redirect("/class_list/")
    return render(request,"add_class.html")

def edit_class(request,id):
    if request.method == "POST":
        # id = request.POST.get("id")
        cname = request.POST.get("cname")
        models.Class.objects.filter(id=id).update(cname=cname)
        return redirect("/class_list/")
    cid = request.GET.get(id)
    class_obj = models.Class.objects.get(id=id)
    return render(request,"edit_class.html",{"class":class_obj})

def search_class(request):
    search_cstr = request.POST.get('search_cstr')
    objs = models.Class.objects.filter(Q(cname__contains=search_cstr)|Q(id__contains=search_cstr))
    return render(request, 'class_list.html', {'class_list': objs})


# 学生页面
def student_list(request):
    data = []
    student_list = models.Student.objects.all()
    for i in student_list:
        data.append(i)

    page_num = request.GET.get("page")
    path = request.path_info
    from tools.mypage import MyPage
    page = MyPage(page_num, len(data), path)
    page_html = page.page_html()
    return render(request,"student_list.html",{"student_list": data[page.start:page.end], "page_html": page_html})

def delete_student(request, sid):
    models.Student.objects.filter(id=sid).delete()
    return redirect(reverse("student_list"))

def add_student(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        cid = request.POST.get("cid")
        models.Student.objects.create(cid_id=cid,sname=sname)
        return redirect(reverse("student_list"))
    class_list = models.Class.objects.all()
    return render(request,'add_student.html',{"class_list":class_list})

def edit_student(request,sid):
    if request.method == "POST":
        sname = request.POST.get("sname")
        cid = request.POST.get("cid")
        models.Student.objects.filter(id=sid).update(sname=sname,cid_id=cid)
        return redirect(reverse("student_list"))
    student_obj = models.Student.objects.get(id=sid)
    class_list = models.Class.objects.all()
    return render(request,'edit_student.html',{"class_list":class_list,"student":student_obj})

def search_student(request):
    search_sstr = request.POST.get('search_sstr')
    objs = models.Student.objects.filter(Q(sname__contains=search_sstr)|Q(id__contains=search_sstr)|Q(cid__cname__contains=search_sstr))

    # student_list = models.Student.objects.all()
    return render(request,'student_list.html',{'student_list':objs})

# 老师页面
def teacher_list(request):
    data = []
    teacher_list = models.Teacher.objects.all()
    for i in teacher_list:
        data.append(i)

    page_num = request.GET.get("page")
    path = request.path_info
    from tools.mypage import MyPage
    page = MyPage(page_num, len(data), path)
    page_html = page.page_html()
    return render(request,'teacher_list.html',{'teacher_list':data[page.start:page.end], "page_html": page_html})

def delete_teacher(request, tid):
    models.Teacher.objects.filter(id=tid).delete()
    return redirect('/teacher_list/')

def add_teacher(request):
    if request.method == "POST":
        tname = request.POST.get("tname")
        class_ids = request.POST.getlist("cid")
        teacher_obj = models.Teacher.objects.create(tname=tname)
        class_objs = models.Class.objects.filter(id__in=class_ids)
        teacher_obj.cid.set(class_objs)
        return redirect(reverse('teacher_list'))
    class_list = models.Class.objects.all()
    return render(request,'add_teacher.html',{"class_list":class_list})

def edit_teacher(request,tid):
    if request.method == "POST":
        tname = request.POST.get("tname")
        models.Teacher.objects.filter(id=tid).update(tname=tname)
        obj = models.Teacher.objects.get(id=tid)
        class_ids = request.POST.getlist("cid")
        obj.cid.set(class_ids)
        return redirect(reverse('teacher_list'))
    teacher_obj = models.Teacher.objects.get(id=tid)
    class_list = models.Class.objects.all()
    return render(request, 'edit_teacher.html', {'teacher': teacher_obj, 'class_list': class_list})

def search_teacher(request):
    search_tstr = request.POST.get('search_tstr')
    objs = models.Teacher.objects.filter(Q(tname__contains=search_tstr)|Q(id__contains=search_tstr)|Q(cid__cname__contains=search_tstr))

    # student_list = models.Student.objects.all()
    return render(request,'teacher_list.html',{'teacher_list':objs})

