#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS=('calaccess_scraped',),
            MIDDLEWARE_CLASSES=()
        )
        from django.core.management import call_command
        import django
        django.setup()
        call_command('test', 'calaccess_scraped')


setup(
    name='django-calaccess-scraped-data',
    version='0.1.0',
    license='MIT',
    description='A Django app to scrape campaign finance data \
from the California Secretary of State’s CAL-ACCESS database',
    url='http://django-calaccess-scraped-data.californiacivicdata.org',
    author='California Civic Data Coalition',
    author_email='cacivicdata@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,  # because we're including static files
    install_requires=(
        'django-calaccess-raw-data>=1.4.7',
        'django>=1.9',
        'csvkit>=1.0',
        'beautifulsoup4>=4.3.2',
    ),
    cmdclass={'test': TestCommand,}
)
