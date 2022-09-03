# Generated by Django 4.1 on 2022-09-02 20:40

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('pfp', '120x240', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
