# Generated by Django 4.0.1 on 2022-04-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_teacher_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
