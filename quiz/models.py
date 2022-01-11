import datetime

import django.utils.timezone
from django.db import models
from lessons.models import Lesson
from school_users.models import UserProfile

TEST_AND_QUESTION_OPTIONS = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
    ('extra-hard', 'extra-hard')
)

QUIZ_REPR = (
    ('match','match'),
    ('true/false', 'true/false'),
    ('open_question', 'open_question'),
    ('general', 'general'),
    ('space_word', 'space_word')
)

XP_REPR = (
    ('50','50'),
    ('65', '65'),
    ('80', '80'),
    ('100', '100')
)

QUIZ_TYPE = (
    ('grammar', 'grammar'),
    ('listening', 'listening'),
    ('reading', 'reading'),
    ('use_of_english', 'use_of_english'),
    ('writing', 'writing'),
)



class Quiz(models.Model):
    vc_name = models.CharField(max_length=170, verbose_name="Название теста")
    i_score_to_pass = models.IntegerField(verbose_name="% для прохождения")
    vc_difficulty = models.CharField(max_length=15, choices=TEST_AND_QUESTION_OPTIONS, verbose_name = 'Сложность')
    i_lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='К какому уроку относится')
    vc_quiz_repr = models.CharField(max_length=20, choices=QUIZ_REPR, verbose_name="Представление теста")
    quiz_type = models.CharField(default='grammar',max_length=20, choices=QUIZ_TYPE, verbose_name="Тип теста")



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Тест")
    dt_created_at = models.DateTimeField(default=django.utils.timezone.now)
    difficulty = models.CharField(max_length=15, choices=TEST_AND_QUESTION_OPTIONS , default='easy')
    xp = models.IntegerField(default=1)



class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name="Вопрос")
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")



class Result(models.Model):
    score = models.FloatField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тесты')
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, verbose_name='Пользователь')

