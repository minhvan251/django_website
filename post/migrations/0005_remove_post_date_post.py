# Generated by Django 3.0.4 on 2020-03-27 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200326_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_post',
        ),
    ]
