# Generated by Django 2.1.15 on 2020-04-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='sweetpotato_num',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='sweetpotato_size',
            field=models.CharField(max_length=30),
        ),
    ]
