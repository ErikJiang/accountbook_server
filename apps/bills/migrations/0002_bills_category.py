# Generated by Django 2.0.5 on 2018-05-10 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorys', '0001_initial'),
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorys.Categorys', verbose_name='明细分类'),
        ),
    ]
