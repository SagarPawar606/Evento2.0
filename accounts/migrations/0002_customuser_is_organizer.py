# Generated by Django 4.1 on 2023-11-02 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_organizer',
            field=models.BooleanField(default=False),
        ),
    ]
