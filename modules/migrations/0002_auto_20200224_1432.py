# Generated by Django 3.0.3 on 2020-02-24 14:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_id', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='tasklist',
            name='sample',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='task_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=15),
        ),
    ]
