# Generated by Django 4.1.4 on 2023-01-03 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='source',
        ),
    ]
