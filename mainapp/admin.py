from django.contrib import admin

from mainapp.models import ProgrammingLanguage, Technology, Course

admin.site.register(ProgrammingLanguage)
admin.site.register(Technology)
admin.site.register(Course)
