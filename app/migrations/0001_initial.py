# Generated by Django 4.1.5 on 2023-07-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fisrtname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_login',
            },
        ),
    ]
