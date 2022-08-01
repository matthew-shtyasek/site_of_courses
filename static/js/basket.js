function setButton(event=null, data) {
    if (event == null) {
        event = $('.btn-remove-add-basket');
    } else {
        event = event.handler;
    }

    if (!data.is_user_authenticated) {
        while (event.firstChild()) {
            event.removeChild(event.firstChild());
        }
        return;
    }

    let a = document.createElement('a');
    a.classList.add('btn');

    if (data.is_in_user_basket) {
        a.classList.add('btn-success');
        a.classList.add('btn-add-to-basket');
        a.href = '{% url \'basket:add_course\' course.pk %}';
        a.text = 'Добавить в козину';
    } else {
        a.classList.add('btn-danger');
        a.classList.add('btn-remove-from-basket');
        a.href = '{% url \'basket:remove_course\' course.pk %}';
        a.text = 'Удалить из козины';
    }
    event.appendChild(a);
}

window.onload = function () {
    $('.btn-remove-add-basket').ready(function () {
        console.log('all good');
        setButton(null, data = {
            is_in_user_basket: '{{ is_in_user_basket }}',
            is_user_authenticated: '{{ user.is_authenticated }}'
        });
    });
    $('.btn-remove-add-basket').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            url: event.handler.href,
            success: function (data) {
                setButton(event, data)
            }
        });
    });
}