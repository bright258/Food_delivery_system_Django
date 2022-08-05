# Generated by Django 4.0 on 2022-08-02 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_orderbid_darsher_alter_orderbid_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='darsher',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='darsher', to='core.customuser'),
        ),
    ]
