from django.shortcuts import render
from myapp import models


# def index(request):
#     list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]
#
#     name = request.POST.get("name", None)
#     password = request.POST.get("password", None)
#     #表单信息放进字典
#     data = {'name':name,'password':password}
#     list.append(data)
#     return render(request, 'index.html', {'form': list})
# -*- coding: utf-8 -*-


from django.http import HttpResponse,HttpResponseRedirect
from myapp import models


def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == "GET":  #如果提交方式为GET即显示login.html
        return render(request, "login.html")
    else:    # 如果提交方式为POST
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        userModel = models.UserModel.objects.filter(username=username, password=password).first()# 数据库验证账号
        # if userModel:  # 如果存在则返回欢迎浏览书店，否则返回用户名或密码错误
        #     return HttpResponse("欢迎浏览书店！")
        # else:
        #     return HttpResponse("用户名或密码错误")
        return HttpResponse(userModel)


def register(request):
    if request.method == "GET":  # 如果提交方式为GET即显示login.html
        return render(request, "register.html")
    else:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserModel.objects.create(username=username, password=password)
        return HttpResponse('OK')
        # return render(request, "login.html")
