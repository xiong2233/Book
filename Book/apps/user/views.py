from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import *
from utils.sendemail import SendEmail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
import re
#将本项目中的forms模块导入进来

def register_views(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  else:
    user = UserInfo()
    email = request.POST.get('email')
    user.email = email
    uemail = UserInfo.objects.filter(email=user.email)
    if uemail:
        return redirect('/register')
    user.name = request.POST.get('name')
    uname = UserInfo.objects.filter(name=user.name)
    if uname:
        return redirect('/register')
    user.password = request.POST.get('password')
    apassword = request.POST.get("confirm_password")
    if len(user.password)<6 or len(user.password)>18:
        return redirect('/register')
    if apassword != user.password:
        return redirect('/register')
    check = request.POST.get("checkbox")
    if check == None:
        return render(request,'register.html',{'error':'请阅读政策条款'})
    send = SendEmail()
    code = send.send_register_email(email)
    user.code = code
    user.save()
    return redirect('/test')
def test(request):
    if request.method == "GET":
        return render(request,"test.html")
    else:
        email = request.POST.get("email")
        code = request.POST.get("code")
        try:
            user = UserInfo.objects.get(email=email,code=code)
            user.is_active = True
            user.save()
            return redirect('/')
        except:
            return render(request,"test.html",{"error":"邮箱或验证码错误"})


def emailajax(request):
    email = request.GET.get('email')
    if email is not None:
        try:
            user = UserInfo.objects.filter(email=email)
            if user:
                return HttpResponse("邮箱已存在请登录")
            else:
                try:
                    validate_email(email)
                    return HttpResponse("成功")
                except ValidationError:
                    return HttpResponse("请输入有效邮箱")
        except Exception as e:
            print(e)
    else:
        return HttpResponse("请输入邮箱")



def userajax(request):
    name = request.GET.get('name')
    username = UserInfo.objects.filter(name=name)
    if len(username)>0:
        return HttpResponse("用户名已存在")
    if name=="":
        return HttpResponse("请输入用户名")
    if username:
        return HttpResponse("用户名已存在")
    return HttpResponse("成功")


def passwordajax(request):
    password = request.GET.get("password")
    if password =="":
        return HttpResponse("请输入密码")
    if 6<=len(password)<=18:
        return HttpResponse("成功")
    else:
        return HttpResponse("请输入6-18位的密码")

def pwdajax(request):
    password = request.GET.get("password")
    pwd = request.GET.get("pwd")
    if pwd =="":
        return HttpResponse("请输入确认密码")
    if password == pwd:
        return HttpResponse("成功")
    else:
        return HttpResponse("确认密码与上面不同")

def login_views(request):
  if request.method == 'GET':
    if 'email' in request.session:
        return redirect('/index')
    else:
        if 'email' in request.COOKIES and 'upwd' in request.COOKIES:

            # cookie中有登录信息的,继续向下判断
            # 从cookie中获取相应的数据
            email = request.COOKIES['email']
            password = request.COOKIES['upwd']
            # 去数据库中判断email和upwd是否正确
            users = UserInfo.objects.filter(email=email, password=password)
            if users:
                # cookies中的数据是正确的
                # 将email的值保存进session,重定向回url
                request.session['email'] = email
                request.session.set_expiry(0)
                return redirect("/index")
            else:
                # cookies中的数据是错误的,删除登录信息,重新回到登录页面
                resp = render(request, 'login.html')
                resp.delete_cookie('email')
                resp.delete_cookie('upwd')
                return resp
        else:
            # cookie中也没有登录信息,则去往登录页面
            # 将请求源地址url封装到cookie中
            resp = render(request, 'login.html')
            return resp
    return render(request,'login.html')
  else:
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        codes = UserInfo.objects.get(email=email)
        active = codes.is_active
        print(type(active))
        if active is False:
            print(4)
            return render(request,'login.html',{'message':"还未激活邮箱"})
        else:
            user = UserInfo.objects.filter(email=email, password=password)
            if user:
                # 登录成功的业务处理
                # 将登录uphone值保存进session
                request.session['email'] = email
                request.session.set_expiry(0)
                # 判断是否要记住密码
                # 创建响应对象
                resp = redirect('/index')
                if 'isactive' in request.POST:
                    max_age = 60 * 60 * 24 * 365
                    resp.set_cookie('email', email, max_age)
                    resp.set_cookie('upwd', password, max_age)
                return resp
            else:
                return render(request, 'login.html', {'message': "邮箱或密码错误"})
    except:
        return render(request,'login.html',{'message':"还未注册邮箱或邮箱填写错误"})


def admin_login(request):
    if request.method == "GET":
        if 'username' in request.session and 'pwd' in request.session:
            return redirect('/adminindex')
        else:
            return render(request,'adminlogin.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Administrator.objects.get(username=username,password=password)
            if user and user.is_active:
                # 登录成功的业务处理
                request.session['username'] = username
                request.session['pwd'] = password
                request.session.set_expiry(0)
                # 判断是否要记住密码
                resp = redirect('/adminindex')
                return resp
            else:
                return render(request, 'adminlogin.html', {'message': "用户名或密码错误"})
        except:
            return render(request, 'adminlogin.html', {'message': "用户名或密码错误"})


def adminlogout(request):
    del request.session["username"]
    del request.session['pwd']
    return HttpResponseRedirect('/adminlogin')






