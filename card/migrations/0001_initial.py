# Generated by Django 5.0.2 on 2024-05-09 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0006_remove_carditem_card_remove_order_card_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_user', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='card.card')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('home', models.TextField()),
                ('flot', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('shopping_list', models.TextField(null=True)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='card.card')),
            ],
        ),
    ]
