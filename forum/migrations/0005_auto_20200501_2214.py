# Generated by Django 3.0.5 on 2020-05-01 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200501_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classe',
            old_name='scuola_appartenenza',
            new_name='scuola',
        ),
        migrations.AddField(
            model_name='sezione',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Classe'),
        ),
    ]