# Generated by Django 4.2.5 on 2024-03-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascent', '0002_newuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
