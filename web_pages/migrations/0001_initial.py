# Generated by Django 4.2.1 on 2023-08-13 17:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('browser_session', models.CharField(max_length=100, unique=True)),
                ('href_to', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('header', models.TextField()),
                ('ip', models.CharField(max_length=60)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('web_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_requests', to='web_pages.webpage')),
            ],
        ),
    ]