# Generated by Django 5.1.5 on 2025-01-29 18:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('quotes', '0003_remove_quote_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='password',
        ),
    ]
