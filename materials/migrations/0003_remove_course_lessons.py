# Generated by Django 5.1.2 on 2024-11-06 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_remove_lesson_link_to_video_course_lessons_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lessons',
        ),
    ]
