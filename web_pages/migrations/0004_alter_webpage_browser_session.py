# Generated by Django 4.2.1 on 2023-08-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pages', '0003_remove_webpage_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='browser_session',
            field=models.CharField(max_length=100),
        ),
    ]