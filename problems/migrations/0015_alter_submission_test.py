# Generated by Django 5.0.6 on 2024-07-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0014_alter_submission_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='test',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
