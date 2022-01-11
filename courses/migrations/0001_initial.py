# Generated by Django 4.0.1 on 2022-01-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_name', models.CharField(max_length=130, verbose_name='Название курса')),
                ('ch_description', models.CharField(max_length=1500, verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'Информация о курсе',
                'verbose_name_plural': 'Информация о курсе',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_name', models.CharField(max_length=100, verbose_name='Название подписки')),
                ('ch_description', models.CharField(max_length=800, verbose_name='Описание подписки')),
                ('fl_price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Тип подписки',
                'verbose_name_plural': 'Тип подписки',
            },
        ),
        migrations.CreateModel(
            name='UserCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_subscription_start', models.DateTimeField(verbose_name='Дата покупки')),
                ('dt_subscription_end', models.DateTimeField(verbose_name='Конец подписки')),
                ('i_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseinfo', verbose_name='Курс')),
                ('i_subscription_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.subscriptiontype', verbose_name='Тип подписки')),
                ('i_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_users.userprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Курс пользователя',
                'verbose_name_plural': 'Курсы пользователя',
            },
        ),
        migrations.CreateModel(
            name='UserRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_xp', models.IntegerField(default=1, verbose_name='XP')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.usercourses', verbose_name='ID пользователя')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинг',
            },
        ),
    ]
