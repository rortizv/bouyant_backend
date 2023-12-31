# Generated by Django 4.2.4 on 2023-08-11 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('ships', '0002_shipaccesories_and_more'),
        ('reviews', '0001_initial'),
        ('reservations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review', verbose_name='Review'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.ship', verbose_name='Ship'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='post',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='posts.post', verbose_name='Post'),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='review',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='reviews.review', verbose_name='Review'),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='ship',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ships.ship', verbose_name='Ship'),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
