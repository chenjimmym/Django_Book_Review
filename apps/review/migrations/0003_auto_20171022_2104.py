# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20171022_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_review',
            name='belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='review.Book'),
        ),
        migrations.RemoveField(
            model_name='book_review',
            name='reviewed_by',
        ),
        migrations.AddField(
            model_name='book_review',
            name='reviewed_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='review.User'),
            preserve_default=False,
        ),
    ]