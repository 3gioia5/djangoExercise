# Generated by Django 2.2 on 2022-07-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0005_auto_20210421_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_domain',
            field=models.CharField(max_length=30, null=True),
        ),
    ]