# Generated by Django 4.0.1 on 2022-01-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_users', '0002_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauth',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
