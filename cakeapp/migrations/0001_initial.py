# Generated by Django 5.0 on 2023-12-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Product_Name')),
                ('price', models.FloatField()),
                ('detail', models.CharField(max_length=100, verbose_name='Product_Detail')),
                ('cat', models.IntegerField(choices=[(1, 'Anniversary Cake'), (2, 'Birthday Cake'), (3, 'Eggless Cake'), (4, 'Kids Cake'), (5, 'Party Cake'), (6, 'Photo Cake'), (7, 'Regular Cake')], verbose_name='Category')),
                ('is_active', models.BooleanField(default=True)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
    ]
