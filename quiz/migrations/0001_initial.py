# Generated by Django 4.0.1 on 2022-01-22 21:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
        ('school_users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('xp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_mistake', models.BooleanField(default=True)),
                ('answer_type', models.CharField(choices=[('grammar', 'grammar'), ('listening', 'listening'), ('reading', 'reading'), ('use_of_english', 'use_of_english'), ('writing', 'writing'), ('correct', 'correct')], max_length=80, verbose_name='Тип ответа')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vc_name', models.CharField(max_length=170, verbose_name='Название теста')),
                ('i_score_to_pass', models.IntegerField(verbose_name='% для прохождения')),
                ('vc_difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard'), ('extra-hard', 'extra-hard')], max_length=15, verbose_name='Сложность')),
                ('vc_quiz_repr', models.CharField(choices=[('match', 'match'), ('true/false', 'true/false'), ('open_question', 'open_question'), ('general', 'general'), ('space_word', 'space_word')], max_length=20, verbose_name='Представление теста')),
                ('quiz_type', models.CharField(choices=[('grammar', 'grammar'), ('listening', 'listening'), ('reading', 'reading'), ('use_of_english', 'use_of_english'), ('writing', 'writing')], default='grammar', max_length=20, verbose_name='Тип теста')),
                ('i_lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='К какому уроку относится')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz', verbose_name='Тесты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_users.userprofile', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ResultMistake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answer', verbose_name='Ответ')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.result', verbose_name='Результат')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vc_name', models.CharField(default='', max_length=90, verbose_name='Вопрос')),
                ('dt_created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard'), ('extra-hard', 'extra-hard')], default='easy', max_length=15)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz', verbose_name='Тест')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.answertype', verbose_name='Тип ошибки'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question', verbose_name='Вопрос'),
        ),
    ]
