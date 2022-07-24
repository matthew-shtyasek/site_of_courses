from django.shortcuts import render

from mainapp.models import Course


def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, template_name='mainapp/index.html', context=context)
