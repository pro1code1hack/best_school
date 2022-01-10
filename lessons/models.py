from django.db import models

# Create your models here.
from courses.models import CourseInfo




class Lesson(models.Model):
    i_course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name="Курс")
    ch_lesson_name = models.CharField(max_length=150, verbose_name='Название урока')
    ch_lesson_text = models.CharField(max_length=3000, verbose_name='Текст урока')
    ch_lesson_plan = models.CharField(max_length=1500, verbose_name='План урока')

    class Meta:
        verbose_name = ("Урок")
        verbose_name_plural = ("Уроки")




