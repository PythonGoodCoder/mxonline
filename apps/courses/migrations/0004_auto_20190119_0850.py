# Generated by Django 2.1.4 on 2019-01-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190119_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='course/201901/default.jpg', null=True, upload_to='course/%Y%m', verbose_name='封面图'),
        ),
    ]
