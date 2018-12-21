# -*- coding: utf-8 -*-
# @Author: Fannie
from django.forms import ModelForm, Select, TextInput
from .models import Vmpzxx

class VmpzxxForm(ModelForm):
    class Meta:
        model = Vmpzxx
        exclude = []

class VmpzxxAddForm(ModelForm):
    class Meta:
        model = Vmpzxx
        exclude = []

        widgets = {
            'vm_name': TextInput( attrs={'class': 'input-text'}),
            'creator': TextInput( attrs={'class': 'input-text'}),
            'user': TextInput( attrs={'class': 'input-text'}),
            'user_gh': TextInput( attrs={'class': 'input-text'}),
            'ssdw': TextInput( attrs={'class': 'input-text'}),
            'office_phone': TextInput( attrs={'class': 'input-text'}),
            'cell_phone': TextInput( attrs={'class': 'input-text'}),
            'use': TextInput( attrs={'class': 'input-text'}),
            'ip': TextInput( attrs={'class': 'input-text'}),
            'mac': TextInput( attrs={'class': 'input-text'}),
            'os': TextInput( attrs={'class': 'input-text'}),
            'cpu_hs': TextInput( attrs={'class': 'input-text'}),
            'memory': TextInput( attrs={'class': 'input-text'}),
            'harddisk': TextInput( attrs={'class': 'input-text'}),
            'create_time': TextInput( attrs={'class': 'input-text'}),
            'zyc': TextInput( attrs={'class': 'input-text'}),
            'vc': TextInput( attrs={'class': 'input-text'}),
            'backup': Select( attrs={'class': 'select', 'style': 'height: 31px; padding: 4px;',}),
            'policy': TextInput( attrs={'class': 'input-text'}),
            'yxq': TextInput( attrs={'class': 'input-text'}),
            'beian': Select( attrs={'class': 'select', 'style': 'height: 31px; padding: 4px;',}),
            'remark': TextInput( attrs={'class': 'input-text'}),
        }