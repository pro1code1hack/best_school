from django.db import models
from django.utils.timezone import utc

from school_users.models import  UserProfile
# Create your models here.


"""
Преподователи 
Кто тд тп
Кто составил тест
кто проверил тест
"""


class CourseInfo(models.Model):
    ch_name = models.CharField(max_length=130 , verbose_name='Название курса')
    ch_description = models.CharField(max_length=1500, verbose_name='Описание курса')

    def __str__(self):
        return "{}".format(self.ch_name)

    class Meta:
        verbose_name_plural = 'Информация о курсе'
        verbose_name = 'Информация о курсе'


class SubscriptionType(models.Model):
    ch_name = models.CharField(max_length=100, verbose_name = 'Название подписки')
    ch_description = models.CharField(max_length=800, verbose_name = 'Описание подписки')
    fl_price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return "{}".format(self.ch_name)

    class Meta:
        verbose_name_plural = 'Тип подписки'
        verbose_name = 'Тип подписки'


class UserCourses(models.Model):
    i_subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE , verbose_name='Тип подписки')
    i_course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name='Курс')
    i_user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь')
    dt_subscription_start = models.DateTimeField(verbose_name='Дата покупки')
    dt_subscription_end = models.DateTimeField(verbose_name='Конец подписки')

    def __str__(self):  # self.i_course_id.ch_name
        return f"{self.i_user_id}"

    class Meta:
        verbose_name_plural = 'Курсы пользователя'
        verbose_name = 'Курс пользователя'


class UserRanking(models.Model):
    user_id = models.ForeignKey(UserCourses, on_delete=models.CASCADE, verbose_name='ID пользователя')
    i_xp = models.IntegerField(default=1, verbose_name='XP')

    class Meta:
        verbose_name_plural = 'Рейтинг'
        verbose_name = 'Рейтинг'

    def __str__(self):  # self.i_course_id.ch_name
        return f"{self.user_id.i_course_id}"        # ээ, тудаа нам надо