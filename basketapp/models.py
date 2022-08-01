from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Course


class CourseBasket(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
