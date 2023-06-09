# Generated by Django 4.1.7 on 2023-03-20 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site1", "0006_remove_model2_pole3_model2_pole4"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=45, verbose_name="Название")),
                ("task", models.TextField(verbose_name="Описание")),
            ],
        ),
        migrations.RemoveField(
            model_name="model2",
            name="pole4",
        ),
        migrations.DeleteModel(
            name="Model1",
        ),
        migrations.DeleteModel(
            name="Model2",
        ),
    ]
