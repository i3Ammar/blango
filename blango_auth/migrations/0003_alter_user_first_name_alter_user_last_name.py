# Generated by Django 5.1.4 on 2025-01-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blango_auth', '0002_alter_user_managers_remove_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
