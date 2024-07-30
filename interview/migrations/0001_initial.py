# Generated by Django 5.0.6 on 2024-07-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=70)),
                ('hr', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=12)),
                ('time', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
