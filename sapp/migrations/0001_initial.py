# Generated by Django 3.0.9 on 2020-08-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(max_length=10)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=25)),
                ('phone', models.IntegerField(blank=True, max_length=15)),
                ('father_name', models.CharField(blank=True, max_length=20)),
                ('mother_name', models.CharField(blank=True, max_length=20)),
                ('cgpa', models.CharField(blank=True, max_length=5)),
            ],
        ),
    ]
