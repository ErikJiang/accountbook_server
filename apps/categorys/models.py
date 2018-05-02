from django.db import models

# Create your models here.
# 分类表
class Categorys(models.Model):
    OUTGO = '0'     # 账目类型.支出
    INCOME = '1'    # 账目类型.收入
    TYPE_CHOICE = (
        (OUTGO, 'OUTGO'),
        (INCOME, 'INCOME'),
    )

    user = models.TextField() # 用户ID ForeignKey()
    is_default = model.BooleanField() # 是否为初始默认类型 True:默认存在分类 False:用户自定义分类
    is_parent = model.BooleanField() # 是否为父类 True:父类 False:子类
    bill_type = models.CharField(max_length=1, choices=TYPE_CHOICE, default=OUTGO) # 账目类型
    name = models.TextField() # 分类名称 
    parent_id = models.TextField() # 父级ID
    modify_time = models.DateTimeField(auto_now=True) # 修改时间
    create_time = models.DateTimeField(auto_now_add=True) # 创建时间

    class Meta:
        db_table = "categorys"
