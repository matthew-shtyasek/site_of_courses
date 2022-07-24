from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'


class Technology(models.Model):
    programming_languages = models.ManyToManyField(ProgrammingLanguage, default=1)

    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология (Фреймворк)'
        verbose_name_plural = 'Технологии (Фреймворки)'


class Course:
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    technologies = models.ManyToManyField(Technology, default=1)

    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
