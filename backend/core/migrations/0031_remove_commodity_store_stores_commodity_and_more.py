# Generated by Django 4.0 on 2022-07-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_remove_order_estimated_duration_of_transit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='store',
        ),
        migrations.AddField(
            model_name='stores',
            name='commodity',
            field=models.ManyToManyField(related_name='commodity', to='core.Commodity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_spot',
            field=models.TextField(max_length=200, verbose_name='delivery_spot'),
        ),
    ]
