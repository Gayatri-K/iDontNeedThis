# Generated by Django 2.2 on 2019-04-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]