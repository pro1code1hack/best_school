import django.utils.timezone
from django.db import models



class UserProfile(models.Model):
    ch_username = models.CharField(max_length=50, unique=True , verbose_name='username')
    ch_password = models.CharField(max_length=60 ,verbose_name='password')           # has to be hashed
    b_is_active = models.BooleanField(default=False , verbose_name='is_active')
    ch_name = models.CharField(max_length=100, verbose_name='Имя')
    ch_surname = models.CharField(max_length=100, verbose_name='Фамилия')
    url_photo = models.URLField(max_length=250, verbose_name='Photo')        # the path to the database
    dt_register_date = models.DateTimeField(verbose_name= 'Дата регистрации',default=django.utils.timezone.now)
    i_confirmation_links_amount = models.IntegerField(default=1) # added
    xp = models.FloatField()
    courses_access_json = models.JSONField()        #  массив значений курсов

    def __str__(self):
        return "{}".format(self.ch_username)




