# Generated by Django 5.0.2 on 2024-07-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myschool", "0002_rename_fiest_name_student_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
    ]