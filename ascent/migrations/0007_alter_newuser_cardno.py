# Generated by Django 4.2.5 on 2024-04-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascent', '0006_remove_newuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='cardno',
            field=models.CharField(max_length=100),
        ),
    ]
