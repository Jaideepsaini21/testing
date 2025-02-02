# Generated by Django 5.0.2 on 2024-07-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myschool", "0008_alter_task_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="teacher_assigned",
            field=models.ManyToManyField(
                blank=True, related_name="teacher_assigned", to="myschool.teacher"
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="class_assigned",
            field=models.ManyToManyField(
                blank=True, related_name="class_assigned", to="myschool.classes"
            ),
        ),
    ]
