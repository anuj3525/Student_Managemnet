# Generated by Django 4.0.4 on 2022-06-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_student_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
