# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_complete', models.DateField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50)),
                ('account_number', models.IntegerField(verbose_name=(12, 13, 14, 15, 16, 17, 18, 19))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('local_delivery', models.BooleanField(default=1)),
                ('city', models.CharField(max_length=255)),
                ('product_category', models.ForeignKey(choices=[('electronics', 'ELECTRONICS'), ('sports', 'SPORTS'), ('home', 'HOME'), ('general', 'GENERAL'), ('clothing', 'CLOTHING')], on_delete=django.db.models.deletion.CASCADE, to='website.Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.TextField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_delivery', models.BooleanField(default=0)),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_people', to='website.Profile')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_people', to='website.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', through='website.Recommendations', to='website.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='orders',
            field=models.ManyToManyField(through='website.UserOrder', to='website.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.PaymentType'),
        ),
    ]
