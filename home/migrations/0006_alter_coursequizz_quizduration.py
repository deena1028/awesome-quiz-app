# Generated by Django 4.2.5 on 2023-09-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_coursequizz_quizduration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursequizz',
            name='quizDuration',
            field=models.DurationField(null=True),
        ),
    ]
