# Generated by Django 5.0.6 on 2024-06-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=34)),
                ('city', models.CharField(max_length=34)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
