# Generated by Django 2.2.8 on 2020-03-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=600)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
