# Generated by Django 4.1.7 on 2023-03-21 09:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("site1", "0007_task_remove_model2_pole4_delete_model1_delete_model2"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"verbose_name": ("Задача",), "verbose_name_plural": "Задачи"},
        ),
    ]
