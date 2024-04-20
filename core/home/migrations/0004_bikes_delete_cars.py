# Generated by Django 4.2.5 on 2023-09-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cars_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=100)),
                ('mileage', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='cars',
        ),
    ]