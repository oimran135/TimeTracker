# Generated by Django 4.1.1 on 2022-09-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0005_alter_project_end_date_alter_project_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
