# Generated by Django 5.0.6 on 2024-06-26 15:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_test_cases'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='submission',
            fields=[
                ('time_stamp', models.DateTimeField(auto_created=True)),
                ('Sub_ID', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('verdict', models.CharField(max_length=20)),
                ('Problem_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
