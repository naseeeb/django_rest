# Generated by Django 5.0.6 on 2024-05-27 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
