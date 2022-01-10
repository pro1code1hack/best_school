from django.db import models


# class UserAuth(models.Model):
#
#
#     def __str__(self):
#         return "{}".format(self.ch_username)


class UserProfile(models.Model):
    ch_username = models.CharField(max_length=50, unique=True , verbose_name='username')
    ch_password = models.CharField(max_length=60 ,verbose_name='password')           # has to be hashed
    b_is_active = models.BooleanField(default=False , verbose_name='is_active')
    ch_name = models.CharField(max_length=100, verbose_name='Имя')
    ch_surname = models.CharField(max_length=100, verbose_name='Фамилия')
    url_photo = models.URLField(max_length=250, verbose_name='Photo')        # the path to the database
    dt_register_date = models.DateTimeField(verbose_name= 'Дата регистрации')
    dt_total_time_on_the_website = models.FloatField(verbose_name ='Всего времени на вебсайте')
    i_confirmation_links_amount = models.IntegerField(default=1) # added
    xp = models.FloatField()
    courses_access_json = models.JSONField()        #  массив значений курсов

    def __str__(self):
        return "{}".format(self.ch_username)


# class MetricsType(models.Model):
#     i_metrics_type = models.IntegerField(verbose_name='Тип метрики')
#     ch_metrics_name = models.CharField(max_length=100, verbose_name='Название метрики')
#
#     def __str__(self):
#         return "{}".format(self.ch_metrics_name)
#
#
# class UserMetrics(models.Model):
#     i_user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name= 'Пользователь')
#     i_metrics_type = models.ForeignKey(MetricsType, on_delete=models.CASCADE , verbose_name= 'Тип метрики')
#     i_metrics_value = models.IntegerField(verbose_name= 'Значение метрики')
#
#     def __str__(self):
#         return "{}".format(self.i_user_id.i_user_id.ch_username)        # вот как нахуй!!!
#


