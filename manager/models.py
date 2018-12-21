# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Vmpzxx(models.Model):
    BACKUP_CHOICES = (
        ('True', '是'),
        ('False', '否'),
    )

    RECORDES_CHOICES = (
        ('not required', '无需备案'),
        ('YES', '是'),
        ('NO', '否'),
    )

    vm_name = models.CharField(u'虚机名称', max_length=20)
    creator = models.CharField(u'创建人', max_length=10)
    user = models.CharField(u'申请人', max_length=10)
    user_gh = models.CharField(u'申请人工号', max_length=10)
    ssdw = models.CharField(u'所属单位', max_length=20)
    office_phone = models.CharField(u'办公电话', blank=True, max_length=20)
    cell_phone = models.CharField(u'手机号码', blank=True, max_length=20)
    use = models.CharField(u'用途', blank=True, max_length=20)
    ip = models.CharField(u'IP地址', max_length=16)
    mac = models.CharField(u'MAC地址', blank=True, max_length=16)
    os = models.CharField(u'操作系统', max_length=20)
    cpu_hs = models.CharField(u'CPU核数', max_length=16)
    memory = models.CharField(u'内存(GB)', max_length=10)
    harddisk = models.CharField(u'硬盘(GB)', max_length=10)
    create_time = models.DateField(u'创建时间', blank=True, null=True)
    zyc = models.CharField(u'所在资源池', blank=True, max_length=20)
    backup = models.CharField(u'是否备份', max_length=20, choices=BACKUP_CHOICES)
    policy = models.CharField(u'备份策略', blank=True, max_length=20)
    yxq = models.CharField(u'延期有效期', max_length=20)
    beian = models.CharField(u'是否备案', blank=True, max_length=20, choices=RECORDES_CHOICES)
    remark = models.CharField(u'备注', blank=True, max_length=200)

    class Meta:
        verbose_name = u'虚拟机配置信息表'
        verbose_name_plural = u'虚拟机配置信息表'
        ordering = ['vm_name', '-create_time']
        unique_together = (('vm_name', 'user_gh'),)

    def __str__(self):
        return self.vm_name