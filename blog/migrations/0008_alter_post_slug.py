# Generated by Django 5.1.4 on 2025-02-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_authorprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
