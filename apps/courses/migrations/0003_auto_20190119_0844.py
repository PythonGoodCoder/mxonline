# Generated by Django 2.1.4 on 2019-01-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='course/%Y%m', verbose_name='封面图'),
        ),
    ]