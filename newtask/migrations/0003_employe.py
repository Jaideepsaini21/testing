# Generated by Django 5.0.7 on 2024-08-07 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newtask", "0002_branch"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employe",
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
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("employeid", models.IntegerField(default=0)),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Employe",
                        to="newtask.branch",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]