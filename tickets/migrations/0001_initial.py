# Generated by Django 5.0.2 on 2024-02-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Device', models.CharField(max_length=100)),
            ],
        ),
    ]
