# Generated by Django 4.0.1 on 2022-04-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_orderform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=57)),
                ('skill', models.CharField(max_length=57)),
                ('email', models.EmailField(max_length=57)),
                ('teammemberimg', models.ImageField(upload_to='komal')),
                ('teaminfo', models.TextField(default='teteteteterterterte')),
            ],
        ),
        migrations.AlterField(
            model_name='orderform',
            name='country',
            field=models.CharField(default='india', max_length=57),
        ),
    ]
