# Generated by Django 5.0.6 on 2024-07-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0013_rename_user_id_save_code_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='test',
            field=models.TextField(blank=True, default=''),
        ),
    ]
