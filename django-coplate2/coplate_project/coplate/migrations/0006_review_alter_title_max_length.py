# Generated by Django 2.2 on 2022-06-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0005_auto_20210421_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=35),
        ),
    ]
