# Generated by Django 3.1.2 on 2020-10-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_payment_intent_id',
            field=models.CharField(default='', max_length=254),
        ),
    ]
