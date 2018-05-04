from django.db import models
from django.contrib.auth.models import User
from apps.categorys.models import Categorys

# Create your models here.
class Bills(models.Model):
    """
    账目信息表
    """
    OUTGO = '0'     # 账目类型.支出
    INCOME = '1'    # 账目类型.收入
    TYPE_CHOICE = (
        (OUTGO, 'OUTGO'),
        (INCOME, 'INCOME'),
    )

    user = models.ForeignKey(User, verbose_name='账目所属用户', blank=True, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField('账目类型', max_length=1, choices=TYPE_CHOICE, default=OUTGO)
    category = models.ForeignKey(Categorys, verbose_name='明细分类', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField('账目金额', max_digits=16, decimal_places=2, default=0)
    record_date = models.DateField('记录时间', auto_now=True)
    remarks = models.CharField('备注信息', max_length=140) # 至多140字
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = "bills"
