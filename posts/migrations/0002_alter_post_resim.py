# Generated by Django 4.1.3 on 2022-12-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resim',
            field=models.FileField(blank=True, upload_to='postlar/'),
        ),
    ]
