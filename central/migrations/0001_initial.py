# Generated by Django 3.0.6 on 2020-05-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_initial', models.CharField(max_length=2, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('year_level', models.CharField(max_length=4)),
                ('program', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('has_voted', models.BooleanField(default=False)),
                ('is_inside', models.BooleanField(default=True)),
            ],
        ),
    ]
