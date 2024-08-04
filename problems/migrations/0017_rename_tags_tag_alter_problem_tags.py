# Generated by Django 5.0.6 on 2024-07-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0016_tags_remove_problem_tags_problem_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(to='problems.tags'),
        ),
    ]
