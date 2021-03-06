# Generated by Django 3.1.6 on 2021-04-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rank', models.DecimalField(decimal_places=1, max_digits=10)),
                ('average_bill', models.IntegerField()),
                ('menu', models.ManyToManyField(related_name='menu', to='landing.Products')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Ресторани',
            },
        ),
    ]
