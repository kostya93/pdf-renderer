# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import pdfrenders.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDFRender',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('update_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'pending'), (2, 'in_progress'), (3, 'success'), (4, 'failed')], db_index=True, default=1)),
                ('url', models.URLField(blank=True, null=True)),
                ('html_file', models.FileField(blank=True, null=True, upload_to=pdfrenders.models.html_upload_to)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to=pdfrenders.models.pdf_upload_to)),
            ],
        ),
    ]
