# Generated by Django 2.2 on 2022-07-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220724_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Категория курсов',
                'verbose_name_plural': 'Категории курсов',
            },
        ),
    ]
