# Generated by Django 4.2.7 on 2023-11-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
