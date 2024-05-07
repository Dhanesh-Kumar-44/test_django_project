# Generated by Django 5.0.5 on 2024-05-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
