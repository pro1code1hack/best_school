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
    ('general', 'general')
)


class Quiz(models.Model):
    vc_name = models.CharField(max_length=170, verbose_name="Название теста")
    i_number_of_questions =  models.IntegerField(verbose_name="Количество вопросов")
    i_score_to_pass = models.IntegerField(verbose_name="% для прохождения")
    vc_difficulty = models.CharField(max_length=15, choices=TEST_AND_QUESTION_OPTIONS, verbose_name = 'Сложность')
    i_lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='К какому уроку относится')
    i_xp = models.IntegerField(verbose_name ="Опыт за тест")
    vc_quiz_repr = models.CharField(max_length=20, choices=QUIZ_REPR, verbose_name="Представление теста")

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Тест")
    dt_created_at = models.DateTimeField(default=django.utils.timezone.now())

class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name="Вопрос")
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    difficulty = models.CharField(max_length=15, choices=TEST_AND_QUESTION_OPTIONS , default='easy')

class Result(models.Model):
    score = models.FloatField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тесты')
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
