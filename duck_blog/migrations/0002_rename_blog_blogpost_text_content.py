# Generated by Django 4.0.3 on 2022-03-22 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duck_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='blog',
            new_name='text_content',
        ),
    ]
