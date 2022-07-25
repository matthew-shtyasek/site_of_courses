from django.shortcuts import render

from mainapp.models import Course, CourseCategory


def index(request):
    categories = CourseCategory.objects.all()
    context = {
        'flipblocks_data_list': categories,
        'top_block_text': 'категории курсов'
    }
    return render(request, template_name='mainapp/index.html', context=context)


def category_page(request, pk):
    courses = Course.objects.filter(course_category_id=pk)
    category = CourseCategory.objects.get(pk=pk)
    context = {
        'top_block_text': f'курсы из категории «{category}»',
        'flipblocks_data_list': courses
    }
    return render(request, 'mainapp/category_page.html', context)
