# Generated by Django 2.2.5 on 2019-10-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191024_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='media/profile-default.jpg', upload_to='profile_picture/'),
        ),
    ]
