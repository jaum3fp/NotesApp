# Generated by Django 5.0 on 2023-12-15 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 10, 40, 53, 661365, tzinfo=datetime.timezone.utc)),
        ),
    ]
