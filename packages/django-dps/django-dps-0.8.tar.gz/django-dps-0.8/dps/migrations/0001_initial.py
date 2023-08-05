# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import dps.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('transaction_type', models.CharField(default=b'Purchase', max_length=16, choices=[(b'Purchase', b'Purchase'), (b'Auth', b'Auth'), (b'Complete', b'Complete'), (b'Refund', b'Refund'), (b'Validate', b'Validate')])),
                ('status', models.CharField(default=b'pending', max_length=16, choices=[(b'pending', b'Pending'), (b'processing', b'Processing'), (b'successful', b'Successful'), (b'failed', b'Failed')])),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('secret', models.CharField(default=dps.models.make_uuid, unique=True, max_length=32, editable=False, db_index=True)),
                ('result', models.TextField(blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ('-created', '-id'),
            },
        ),
    ]
