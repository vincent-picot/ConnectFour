# Generated by Django 2.1.7 on 2019-03-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190305_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price_ebook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price_used',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='rent_ebook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rent_new',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rent_used',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
