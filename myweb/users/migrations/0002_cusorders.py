# Generated by Django 4.2.7 on 2023-12-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusOrders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_code', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
