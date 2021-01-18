# Generated by Django 3.1.4 on 2021-01-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransportationFeeListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_city', models.CharField(max_length=255, verbose_name='Send City')),
                ('receiver_city', models.CharField(max_length=255, verbose_name='Receiver City')),
                ('weight_fee', models.FloatField(default=0, verbose_name='Weight Fee')),
                ('volume_fee', models.FloatField(default=0, verbose_name='Volume Fee')),
                ('min_payment', models.FloatField(default=0, verbose_name='Min Payment')),
                ('transportation_supplier', models.CharField(max_length=255, verbose_name='Transportation Supplier')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'transportationfee',
                'ordering': ['-id'],
            },
        ),
    ]
