# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from mypaginator import MyPaginator
from .models import Vmpzxx
from .forms import VmpzxxAddForm, VmpzxxForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger
import xlrd
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

# Create your views here.
# 登录主页面，虚机配置主页面
@login_required
def vmpzm(request):
    if request.method == 'GET':
        vmpzxx_list = Vmpzxx.objects.filter()

        # 搜索
        #虚机名称
        vm_name = request.GET.get('vm_name')
        #创建人
        creator = request.GET.get('creator')
        #申请使用人
        user = request.GET.get('user')
        #申请人工号
        user_gh = request.GET.get('user_gh')
        #申请人单位
        ssdw = request.GET.get('ssdw')
        ip = request.GET.get('ip')
        #操作系统
        os = request.GET.get('os')
        #是否备份
        backup = request.GET.get('backup')
        #是否备案
        beian = request.GET.get('beian')
        if vm_name:
            vmpzxx_list = vm_name.filter(vm_name__contains=vm_name)
        if creator:
            vmpzxx_list = vmpzxx_list.filter(creator__contains=creator)
        if user:
            vmpzxx_list = vmpzxx_list.filter(user__contains=user)
        if user_gh:
            vmpzxx_list = vmpzxx_list.filter(user_gh__contains=user_gh)
        if ssdw:
            vmpzxx_list = vmpzxx_list.filter(ssdw__contains=ssdw)
        if ip:
            vmpzxx_list = vmpzxx_list.filter(ip__contains=ip)
        if os:
            vmpzxx_list = vmpzxx_list.filter(os__contains=os)
        if backup:
            vmpzxx_list = vmpzxx_list.filter(backup__contains=backup)
        if beian:
            vmpzxx_list = vmpzxx_list.filter(beian__contains=beian)

        # 显示虚机配置信息列表
        paginator = MyPaginator(vmpzxx_list, 20, 1)
        page = request.GET.get('page')
        try:
            cur_vmpzxx_list = paginator.page(page)
        except PageNotAnInteger:
            cur_vmpzxx_list = paginator.page(1)
        except EmptyPage:
            cur_vmpzxx_list = paginator.page(paginator.num_pages)

        vmpzxx_add_form = VmpzxxAddForm()
        dicts = {
            'cur_vmpzxx_list': cur_vmpzxx_list,
            'vmpzxx_add_form': vmpzxx_add_form,
        }
        return render(request, 'manager/manager.html', dicts)

    if request.method == 'POST':
        # 添加虚机配置信息
        vmpzxx_add_form = VmpzxxAddForm(request.POST)
        if vmpzxx_add_form.is_valid():
            vmpzxx_add_form.save()
        else:
            print(vmpzxx_add_form.errors.as_json())
        return HttpResponseRedirect(reverse('manager:vmpzm'))

# 删除虚机配置信息
@login_required
def vmpzxx_rem(request, vmpzxx_id):
    Vmpzxx.objects.get(pk=vmpzxx_id).delete()
    return HttpResponseRedirect(reverse('manager:vmpzm'))

#导入虚机配置信息
@login_required
def upload(request):
    if request.method == 'POST':
        excel = request.FILES['upload_excel']
        wb = xlrd.open_workbook(filename=None, file_contents=excel.read())
        table = wb.sheets()[0]
        nrows = table.nrows  # 行数
        ncole = table.ncols  # 列数

        for i in range(1, nrows):
            row_values = table.row_values(i) #一行的数据
            vmpzxx = Vmpzxx()
            vmpzxx.vm_name = row_values[0]
            vmpzxx.creator = row_values[1]
            vmpzxx.user = row_values[2]
            vmpzxx.user_gh = row_values[3]
            vmpzxx.ssdw = row_values[4]
            vmpzxx.office_phone = row_values[5]
            vmpzxx.cell_phone = row_values[6]
            vmpzxx.use = row_values[7]
            vmpzxx.ip = row_values[8]
            vmpzxx.mac = row_values[9]
            vmpzxx.os = row_values[10]
            vmpzxx.cpu_hs = row_values[11]
            vmpzxx.memory = row_values[12]
            vmpzxx.harddisk = row_values[13]
            vmpzxx.create_time = row_values[14]
            vmpzxx.zyc = row_values[15]
            vmpzxx.vc = row_values[16]
            vmpzxx.backup = row_values[17]
            vmpzxx.policy = row_values[18]
            vmpzxx.yxq = row_values[19]
            vmpzxx.beian = row_values[20]
            vmpzxx.remark = row_values[21]
            vmpzxx.save()
        return HttpResponseRedirect(reverse('manager:vmpzm'))

# 批量删除虚机配置信息
@login_required
def vmpzxx_batch_rem(request):
    ids = request.POST.getlist('vmpzxx_check')
    idstring = ','.join(ids)
    Vmpzxx.objects.extra(where=['id IN (' + idstring + ')']).delete()
    return HttpResponseRedirect(reverse('manager:vmpzm'))

# 修改虚机配置信息
@login_required
def vmpzxx_change(request, vmpzxx_id):
    vmpzxx = get_object_or_404(Vmpzxx, pk=vmpzxx_id)
    if request.method == "GET":
        vmpzxx_form = VmpzxxAddForm(instance=vmpzxx)
        return render(request, 'manager/vmpzxx_change.html',
                      {'vmpzxx_form': vmpzxx_form, 'vmpzxx_id': vmpzxx_id, })
    else:
        vmpzxx_form = VmpzxxAddForm(request.POST, instance=vmpzxx)
        if vmpzxx_form.is_valid():
            vmpzxx_form.save()
        else:
            print(vmpzxx_form.errors.as_json())
        return HttpResponseRedirect(reverse('manager:vmpzm'))