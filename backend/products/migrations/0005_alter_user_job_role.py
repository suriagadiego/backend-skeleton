# Generated by Django 4.0 on 2022-08-20 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_brand_created_at_alter_brand_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job_role',
            field=models.ForeignKey(db_column='job_role', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.jobrole', to_field='job_role'),
        ),
    ]
