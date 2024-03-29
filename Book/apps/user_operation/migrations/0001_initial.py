# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-16 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('book_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=datetime.datetime.now, verbose_name='借书时间')),
                ('is_back', models.BooleanField(default=False, verbose_name='是否返还')),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_list.BookList', verbose_name='书名')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='用户')),
            ],
            options={
                'verbose_name': '租借书籍',
                'verbose_name_plural': '租借书籍',
            },
        ),
        migrations.CreateModel(
            name='UserReturnBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='还书时间')),
                ('borrow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_operation.UserOperation')),
            ],
            options={
                'verbose_name': '返还书籍',
                'verbose_name_plural': '返还书籍',
            },
        ),
    ]
