# Generated by Django 2.2 on 2022-07-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_course_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='img\\default.jpg', upload_to='img'),
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='image',
            field=models.ImageField(default='img\\default.jpg', upload_to='img'),
        ),
    ]
