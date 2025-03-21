# Generated by Django 5.1.6 on 2025-03-08 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_of_day', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
                ('todo', models.CharField(max_length=50)),
                ('postit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.postit')),
            ],
        ),
    ]
