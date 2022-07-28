from django.shortcuts import render


def index(request):
    courses = []
    context = {
        'page_title': 'Корзина',
        'top_block_text': f'Ваша корзина, {request.user.username}',
        'courses': courses,
        'outer_request_url': 'main:course_page',
    }
    return render(request, template_name='basketapp/basket_page.html', context=context)
