# Generated by Django 4.0.1 on 2022-01-08 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_userranking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userranking',
            name='xp',
        ),
        migrations.AddField(
            model_name='userranking',
            name='i_xp',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userranking',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.usercourses'),
        ),
    ]
