# Generated by Django 4.1.7 on 2023-03-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
