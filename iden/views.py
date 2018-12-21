# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout

# Create your views here.

#登录
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('manager:vmmanage'))
        else:
            dicts = {
                'login_error': '用户名或密码错误。',
            }
            return render(request, 'iden/login.html', dicts)
    else:
        return render(request, 'iden/login.html')

#注销
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iden:login'))