# Generated by Django 5.0.6 on 2024-06-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_submission_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='problem',
            name='solved',
            field=models.IntegerField(default=0),
        ),
    ]
