# Generated by Django 4.0.1 on 2022-04-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_attendence_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
