# Generated by Django 3.0.7 on 2020-07-10 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200710_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='publish', to='p_library.Publishing'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='debeter',
        ),
        migrations.AddField(
            model_name='book',
            name='debeter',
            field=models.ManyToManyField(through='p_library.Exchange', to='p_library.Friend'),
        ),
    ]
