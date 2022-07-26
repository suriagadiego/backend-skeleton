# Generated by Django 4.0 on 2022-08-18 07:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import products.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='null', max_length=125, unique=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 190735))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 190780))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(default='null', max_length=125, unique=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 191168))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 191181))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(default='null', max_length=125, unique=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 189794))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 189825))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(default='null', max_length=125, unique=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 190512))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 190523))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(default='null', max_length=125, unique=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 190241))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 190271))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_no', models.CharField(default='null', max_length=125, unique=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 192043))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 192059))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 192514)),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='remaining_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 192489)),
        ),
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(max_length=254)),
                ('employee_id', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('first_name', models.CharField(max_length=120)),
                ('middle_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('joined_on', models.DateTimeField(blank=True, null=True)),
                ('job_role', models.ForeignKey(db_column='job_role', on_delete=django.db.models.deletion.DO_NOTHING, to='products.jobrole', to_field='job_role')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 7, 32, 23, 192973))),
                ('invoice_no', models.CharField(default=products.models.invoice_number, max_length=120)),
                ('action', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.user')),
                ('warehouse_no', models.ForeignKey(db_column='warehouse_no', on_delete=django.db.models.deletion.DO_NOTHING, to='products.warehouse', to_field='warehouse_no')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(db_column='brand', default='null', on_delete=django.db.models.deletion.DO_NOTHING, to='products.brand', to_field='brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='other_part_no',
            field=models.ForeignKey(db_column='other_part_no', default='null', on_delete=django.db.models.deletion.DO_NOTHING, related_name='other_part', to='products.partno', to_field='part_no'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='part_no',
            field=models.ForeignKey(db_column='part_no', default='null', on_delete=django.db.models.deletion.DO_NOTHING, related_name='part', to='products.partno', to_field='part_no'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(db_column='supplier', default='null', on_delete=django.db.models.deletion.DO_NOTHING, to='products.supplier', to_field='supplier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(db_column='unit', default='null', on_delete=django.db.models.deletion.DO_NOTHING, to='products.unit', to_field='unit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse_no',
            field=models.ForeignKey(db_column='warehouse_no', default='null', on_delete=django.db.models.deletion.DO_NOTHING, to='products.warehouse', to_field='warehouse_no'),
            preserve_default=False,
        ),
    ]
