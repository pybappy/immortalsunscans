# Generated by Django 2.0 on 2020-09-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200805_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(default=0),
        ),
    ]
