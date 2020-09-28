# -*- coding: utf-8 -*-
from django.db import models


# class UserLoanOrder(models.Model):
#     id = models.AutoField(primary_key=True)
#     iv = models.IntegerField(default=0)
#     psi = models.IntegerField(default=0)
#
#     class Meta:
#         app_label = "myapp"
#         db_table = "test"
# verbose_name = '变量iv值'
# verbose_name_plural = verbose_name


# Create your models here.
class UserModel(models.Model):  # 创建userModel表  用户表
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
