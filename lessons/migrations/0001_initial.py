# Generated by Django 4.0.1 on 2022-01-22 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=120, verbose_name='Название темы')),
                ('i_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseinfo', verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_lesson_name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('ch_lesson_text', models.CharField(max_length=3000, verbose_name='Текст урока')),
                ('ch_lesson_plan', models.CharField(max_length=1500, verbose_name='План урока')),
                ('topic', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lessons.topic', verbose_name='Название темы')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
