# Generated by Django 5.0.6 on 2024-06-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contest',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('contest_ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('number_of_problems', models.IntegerField()),
            ],
        ),
    ]
