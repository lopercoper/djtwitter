# Generated by Django 4.1 on 2022-09-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='primary_key',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]