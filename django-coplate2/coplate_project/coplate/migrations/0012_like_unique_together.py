# Generated by Django 2.2 on 2022-07-14 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('coplate', '0011_change_reverse_relationships'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'content_type', 'object_id')},
        ),
    ]
