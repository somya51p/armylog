# Generated by Django 2.2 on 2020-01-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialno', models.TextField()),
                ('nomenclature', models.TextField()),
                ('quantityrecieved', models.TextField()),
                ('wtratio', models.TextField()),
                ('subdepot', models.TextField()),
            ],
        ),
    ]
