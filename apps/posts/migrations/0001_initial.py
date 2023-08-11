# Generated by Django 4.2.4 on 2023-08-11 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ships', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Deleted at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('journey', models.CharField(max_length=255, verbose_name='Journey')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('discount', models.IntegerField(verbose_name='Discount')),
                ('description', models.TextField(verbose_name='Description')),
                ('ship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.ship', verbose_name='Ship')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPost',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, verbose_name='Deleted at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('journey', models.CharField(max_length=255, verbose_name='Journey')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('discount', models.IntegerField(verbose_name='Discount')),
                ('description', models.TextField(verbose_name='Description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('ship_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ships.ship', verbose_name='Ship')),
            ],
            options={
                'verbose_name': 'historical Post',
                'verbose_name_plural': 'historical Posts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
