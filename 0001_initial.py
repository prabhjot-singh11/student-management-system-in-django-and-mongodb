# Generated by Django 3.2.9 on 2021-12-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('Roll_no', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('contect', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=300)),
                ('course', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
    ]
