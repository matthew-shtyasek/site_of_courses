# Generated by Django 2.2 on 2022-07-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='mainapp.Technology'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='programming_languages',
            field=models.ManyToManyField(to='mainapp.ProgrammingLanguage'),
        ),
    ]
