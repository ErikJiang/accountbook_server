from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorys(models.Model):
    """
    账目明细分类表
    """
    OUTGO = '0'     # 账目类型.支出
    INCOME = '1'    # 账目类型.收入
    TYPE_CHOICE = (
        (OUTGO, 'OUTGO'),
        (INCOME, 'INCOME'),
    )

    is_default = models.BooleanField('是否默认分类', default=True) # True:默认存在分类 False:用户自定义分类
    user = models.ForeignKey(User, verbose_name='自定义分类所属用户', blank=True, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField('账目类型', max_length=1, choices=TYPE_CHOICE, default=OUTGO)
    name = models.CharField('分类名称', max_length=20, unique=True) 
    parent = models.ForeignKey('self', verbose_name='父级分类', blank=True, null=True, on_delete=models.CASCADE)
    modify_time = models.DateTimeField('修改时间', auto_now=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = "categorys"
