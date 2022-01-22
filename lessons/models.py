from django.db import models

# Create your models here.
from courses.models import CourseInfo


class Topic(models.Model):
    topic_name = models.CharField(max_length=120, verbose_name="Название темы", null=False)
    i_course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.topic_name}"


class Lesson(models.Model):
    ch_lesson_name = models.CharField(max_length=150, verbose_name='Название урока')
    ch_lesson_text = models.CharField(max_length=3000, verbose_name='Текст урока')
    ch_lesson_plan = models.CharField(max_length=1500, verbose_name='План урока')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Название темы", default="")

    def __str__(self):
        return f"{self.ch_lesson_name}"

    class Meta:
        verbose_name = ("Урок")
        verbose_name_plural = ("Уроки")
