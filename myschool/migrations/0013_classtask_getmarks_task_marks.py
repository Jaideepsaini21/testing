# Generated by Django 5.0.2 on 2024-08-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "myschool",
            "0012_remove_classtask_title_remove_task_student_assigned_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="classtask",
            name="getmarks",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="task",
            name="marks",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
