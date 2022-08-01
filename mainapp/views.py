from django.shortcuts import render

from basketapp.models import CourseBasket
from mainapp.models import Course, CourseCategory


def index(request):
    categories = CourseCategory.objects.all()
    name = 'категории курсов'
    context = {
        'page_title': name,
        'flipblocks_data_list': categories,
        'top_block_text': name,
        'outer_request_url': 'main:category_page',
    }
    return render(request, template_name='mainapp/index.html', context=context)


def category_page(request, pk):
    courses = Course.objects.filter(course_category_id=pk)
    category = CourseCategory.objects.get(pk=pk)
    name = f'курсы из категории «{category}»'
    context = {
        'page_title': name,
        'top_block_text': name,
        'flipblocks_data_list': courses,
        'outer_request_url': 'main:course_page',
    }
    return render(request, template_name='mainapp/category_page.html', context=context)


def course_page(request, pk):
    course = Course.objects.get(pk=pk)

    if request.user.is_authenticated:
        course_user_basket = CourseBasket.objects.filter(user=request.user)
        in_user_basket = len(course_user_basket.filter(course_id=course.id)) > 0
    else:
        in_user_basket = False

    name = f'курс «{course}»'
    context = {
        'page_title': name,
        'course': course,
        'top_block_text': name,
        'in_user_basket': in_user_basket,
    }
    return render(request, template_name='mainapp/course_page.html', context=context)
