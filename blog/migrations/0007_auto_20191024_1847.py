# Generated by Django 2.2.5 on 2019-10-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='feautured_image',
            field=models.ImageField(default='blog-default.jpg', upload_to='feautured_images/'),
        ),
    ]
