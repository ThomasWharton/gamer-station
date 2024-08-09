# Generated by Django 3.2.25 on 2024-08-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='placeholder subject', max_length=120)),
                ('content', models.TextField(default='placeholder content')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.EmailField(max_length=60, unique=True)),
            ],
        ),
    ]