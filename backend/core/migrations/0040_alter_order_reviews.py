# Generated by Django 4.0 on 2022-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_orderbid_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reviews',
            field=models.ManyToManyField(blank=True, related_name='reviewss', to='core.Reviews'),
        ),
    ]
