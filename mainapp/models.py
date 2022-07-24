from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)


class Technology(models.Model):
    programming_languages = models.ManyToManyField(ProgrammingLanguage, default=1)

    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)


class Course:
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    technologies = models.ManyToManyField(Technology, default=1)

    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)
