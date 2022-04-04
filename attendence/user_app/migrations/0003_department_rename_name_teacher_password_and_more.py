# Generated by Django 4.0.1 on 2022-04-04 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_rename_user_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='time',
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=1, null=True)),
                ('period', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.department')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.ManyToManyField(to='user_app.Department'),
        ),
    ]
