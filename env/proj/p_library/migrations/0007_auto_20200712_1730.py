# Generated by Django 3.0.7 on 2020-07-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20200712_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='debeter',
            field=models.ManyToManyField(blank=True, through='p_library.Exchange', to='p_library.Friend'),
        ),
    ]
