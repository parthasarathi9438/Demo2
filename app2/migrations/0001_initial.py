# Generated by Django 4.0 on 2022-05-31 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50, unique=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
