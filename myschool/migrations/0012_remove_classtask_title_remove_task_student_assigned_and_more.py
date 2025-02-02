# Generated by Django 5.0.7 on 2024-07-31 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myschool", "0011_classtask"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="classtask",
            name="title",
        ),
        migrations.RemoveField(
            model_name="task",
            name="student_assigned",
        ),
        migrations.AddField(
            model_name="classtask",
            name="student",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="myschool.student",
            ),
        ),
        migrations.AlterField(
            model_name="classtask",
            name="task_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_id",
                to="myschool.task",
            ),
        ),
    ]
