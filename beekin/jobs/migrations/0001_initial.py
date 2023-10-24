# Generated by Django 4.2.6 on 2023-10-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('new', models.CharField(max_length=200)),
                ('featured', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('postedAt', models.CharField(max_length=200)),
                ('contract', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('languages', models.CharField(max_length=200)),
                ('tools', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
