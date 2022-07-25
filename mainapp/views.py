from django.shortcuts import render

from mainapp.models import Course, CourseCategory


def index(request):
    categories = CourseCategory.objects.all()
    name = 'категории курсов'
    context = {
        'flipblocks_data_list': categories,
        'title_of_page': name,
        'top_block_text': name
    }
    return render(request, template_name='mainapp/index.html', context=context)


def category_page(request, pk):
    courses = Course.objects.filter(course_category_id=pk)
    category = CourseCategory.objects.get(pk=pk)
    name = f'курсы из категории «{category}»'
    context = {
        'caption_of_page': name,
        'top_block_text': name,
        'flipblocks_data_list': courses
    }
    return render(request, template_name='mainapp/category_page.html', context=context)


def course_page(request, pk):
    course = Course.objects.get(pk=pk)
    name = f'курс «{course}»'
    context = {
        'course': course,
        'caption_of_page': name,
        'top_block_text': name
    }
    return render(request, template_name='mainapp/course_page.html', context=context)
