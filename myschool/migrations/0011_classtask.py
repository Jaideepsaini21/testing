# Generated by Django 5.0.7 on 2024-07-30 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myschool", "0010_remove_task_class_assigned_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("C", "Complete"),
                            ("NC", "Not Complete"),
                            ("P", "Pending"),
                            ("IP", "In Progress"),
                        ],
                        default="P",
                        max_length=2,
                    ),
                ),
                (
                    "task_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_id",
                        to="myschool.task",
                    ),
                ),
            ],
        ),
    ]
