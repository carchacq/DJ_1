# Generated by Django 4.1.6 on 2023-02-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=None)),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
