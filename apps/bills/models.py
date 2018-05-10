from django.db import models
# from django.contrib.auth.models import User
from apps.users.models import CustomUser
from apps.categorys.models import BillType, Categorys
from datetime import date

# 引入Enum类型
from enumfields import EnumIntegerField

# Create your models here.
class Bills(models.Model):
    """
    账目信息表
    """

    user = models.ForeignKey(CustomUser, verbose_name='账目所属用户', blank=True, null=True, on_delete=models.CASCADE)
    bill_type = EnumIntegerField(BillType, verbose_name='账目类型', default=BillType.OUTGO)
    category = models.ForeignKey(Categorys, verbose_name='明细分类', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField('账目金额', max_digits=16, decimal_places=2, default=0)
    record_date = models.DateField('记录时间', default=date.today)
    remarks = models.CharField('备注信息', max_length=140) # 至多140字
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = "bills"
        ordering = ['-modify_time']