# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings

from django.db import migrations


def create_static_page_category(apps, schema_editor):
    Category = apps.get_model('cfblog', 'Category')
    print '\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print 'Creating the static pages category'
    if Category.objects.filter(id=1):
        warnings.warn(
            "Entry for static pages already exists."
        )
    else:
        Category.objects.create(
            id=1,
            title='Static Page',
            description='All the standalone pages should be under this category'
        )
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'


def delete_static_page_category(apps, schema_editor):
    Category = apps.get_model('cfblog', 'Category')
    categories = Category.objects.filter(id=1)
    print '\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print 'Deleting the static pages category'
    if categories:
        categories.delete()
    else:
        warnings.warn(
            "Entry for static pages does not exist."
        )
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'


class Migration(migrations.Migration):

    dependencies = [
        ('cfblog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=create_static_page_category,
            reverse_code=delete_static_page_category
        )
    ]
