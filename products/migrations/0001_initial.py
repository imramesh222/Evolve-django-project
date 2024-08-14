# Generated by Django 5.1 on 2024-08-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('favicon', models.CharField(max_length=500)),
                ('logo', models.CharField(max_length=500)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
