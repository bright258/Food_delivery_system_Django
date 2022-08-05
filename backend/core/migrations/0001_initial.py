# Generated by Django 4.0 on 2022-07-18 21:38

import core.managers
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.managers.CustomManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('top_city', models.BooleanField(default=False, verbose_name='top')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('trending', models.BooleanField(default=False, verbose_name='trending')),
                ('description', models.CharField(max_length=500, verbose_name='description')),
                ('image', models.ImageField(upload_to='then')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=200, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last_name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='core.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Darsher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='darsher', to='core.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('status', models.CharField(choices=[('Delivering now!', 'Active'), ('Coming soon', 'Comingsoon'), ('Delivering in 10 min', 'Soon')], default='Delivering now!', max_length=200, verbose_name='status')),
                ('image', models.ImageField(upload_to='then')),
                ('favorite', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='core.city')),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='core.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_creation_of_order', models.DateTimeField(auto_now_add=True)),
                ('estimated_duration_of_transit', models.TimeField()),
                ('delivery_spot', models.CharField(max_length=200)),
                ('status_of_order', models.CharField(choices=[('Out for delivery', 'Out'), ('Close by', 'Closeby'), ('Order has arrived', 'Arrived'), ('Order was successful', 'Successful')], max_length=200, verbose_name='status')),
                ('proposed_arrival_time', models.DateTimeField(auto_now_add=True)),
                ('time_arrived', models.DateTimeField(auto_now_add=True)),
                ('reviews', models.CharField(max_length=200, verbose_name='reviews')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='core.consumer')),
                ('darsher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='darsher', to='core.darsher')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='core.commodity')),
            ],
        ),
        migrations.AddField(
            model_name='commodity',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='core.stores'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='core.country'),
        ),
    ]
