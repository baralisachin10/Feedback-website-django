# Generated by Django 4.1.3 on 2023-08-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
