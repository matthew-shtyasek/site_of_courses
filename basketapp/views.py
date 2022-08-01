from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from basketapp.models import CourseBasket
from mainapp.models import Course


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:index'))
    courses = Course.objects.filter(coursebasket__user=request.user)
    context = {
        'page_title': 'Корзина',
        'top_block_text': f'Ваша корзина, {request.user.username}',
        'courses': courses,
        'outer_request_url': 'main:course_page',
    }
    return render(request, template_name='basketapp/basket_page.html', context=context)


def add(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:index'))
    course_basket = CourseBasket()
    course = Course.objects.get(pk=pk)
    CourseBasket.objects.get_or_create(user=request.user,
                                        course=course)
    return HttpResponseRedirect(
        reverse('main:category_page',
                kwargs={'pk': course.course_category_id})
    )


def remove(request, course_pk):
    if request.is_ajax():
        course_basket = CourseBasket.objects.get(course_id=course_pk)
        course_basket.delete()
        return JsonResponse({
            'course_pk': course_pk
        })
