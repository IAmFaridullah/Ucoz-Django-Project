# Generated by Django 4.2.1 on 2023-05-30 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('cms', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=30)),
                ('email', models.TextField(max_length=25)),
                ('father_name', models.TextField(max_length=30)),
                ('dept', models.TextField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
    ]
