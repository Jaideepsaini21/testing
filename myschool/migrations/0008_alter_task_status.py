# Generated by Django 5.0.2 on 2024-07-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myschool", "0007_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
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
    ]
