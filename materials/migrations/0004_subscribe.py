# Generated by Django 5.1.2 on 2024-11-11 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_remove_course_lessons'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_to_course', models.ForeignKey(blank=True, help_text='Выберите курс из списка', null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Курс')),
                ('link_to_user', models.ForeignKey(blank=True, help_text='Выберите пользователя из списка', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
    ]