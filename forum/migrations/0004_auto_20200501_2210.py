# Generated by Django 3.0.5 on 2020-05-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20200501_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='url_calendar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='classe',
            name='url_feedback',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
