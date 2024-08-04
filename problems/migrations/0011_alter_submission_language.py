# Generated by Django 5.0.6 on 2024-07-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0010_alter_submission_code_alter_submission_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.CharField(choices=[('cpp', 'C++'), ('py', 'Python'), ('js', 'JavaScript'), ('c', 'C')], default='c++', max_length=20),
        ),
    ]
