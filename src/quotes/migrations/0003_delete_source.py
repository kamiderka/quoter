# Generated by Django 4.1.4 on 2023-01-04 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_remove_quote_source'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Source',
        ),
    ]
