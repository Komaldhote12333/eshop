# Generated by Django 4.0.1 on 2022-04-26 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_remove_contact_information_contact_imformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=57)),
                ('lastnam', models.CharField(max_length=57)),
                ('country', models.CharField(max_length=57)),
                ('housnum', models.CharField(max_length=57)),
                ('city', models.CharField(max_length=57)),
                ('state', models.CharField(max_length=57)),
                ('zipcode', models.CharField(max_length=57)),
                ('phone', models.CharField(max_length=57)),
                ('email', models.CharField(max_length=57)),
                ('additninal', models.CharField(max_length=57)),
                ('price', models.CharField(max_length=57)),
                ('quntity', models.CharField(max_length=57)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
