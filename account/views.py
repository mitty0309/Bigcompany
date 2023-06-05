from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
# login authentication
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

def mypage(request):
  if request.user.is_authenticated:
    name = request.user.username
  return render(request, "account/mypage.html", locals())


def login(request):
  if request.method == 'POST':
    name = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=name, password=password)
    if user is not None:
      if user.is_active:
        auth.login(request, user)
        return redirect('/mypage/')
        mess = '登入成功！'
      else:
        mess = '帳號尚未啟用！'
    else:
      mess = '登入失敗！'
  return render(request, "account/login.html", locals())


def logout(request):
  auth.logout(request)
  return redirect('/mypage/')


def register(request):
  if request.method == "POST":  #如果是以POST方式才處理
    username = request.POST['username']  #取得表單輸入資料
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name  # 姓名
    user.last_name = last_name  # 姓氏
    user.save()
    return redirect('/login/')
  else:
    mess = '請輸入資料'
  return render(request, "account/register.html", locals())