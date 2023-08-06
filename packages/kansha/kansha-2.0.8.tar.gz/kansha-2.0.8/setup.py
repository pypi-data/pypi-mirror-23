# -*- coding:utf-8 -*-
#--
# Copyright (c) 2012-2015 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
#--

from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='kansha',
    version=version,
    author='Net-ng',
    author_email='contact@net-ng.com',
    description='Manage and share collaborative pinboards on the web.',
    long_description=long_description,
    license='BSD',
    keywords='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.cfg', '*.ini', '*.jpg']},
    zip_safe=False,
    install_requires=(
        'alembic',
        'Babel',
        'dateutils',
        'docutils',
        'flup==1.0.2',
        'identicon',
        'nagare[database,i18n]==0.4.1.post473',
        'nagare-services',
        'oauth2==1.5.211',
        'Paste',
        'Pillow',
        'pycrypto',
        'requests',
        'SQLAlchemy',
        'xlwt',
    ),
    dependency_links=[path.join(here, 'vendors'), 'http://www.nagare.org/snapshots/'],
    extras_require={'test': ('nose',),
                    'htmldocs': ('sphinx',),
                    'debug': ('WebError',),
                    'ldap': ('python-ldap',),
                    'postgres': ('psycopg2',),
                    'mysql': ('oursql',),
                    'elastic': ('elasticsearch',)},
    message_extractors={'kansha': [('**.py', 'python', None)]},
    entry_points="""
      [console_scripts]
      kansha-admin = kansha.app:run

      [kansha.commands]
      alembic-current = kansha.alembic.admin:AlembicCurrentCommand
      alembic-downgrade = kansha.alembic.admin:AlembicDowngradeCommand
      alembic-revision = kansha.alembic.admin:AlembicRevisionCommand
      alembic-stamp = kansha.alembic.admin:AlembicStampCommand
      alembic-upgrade = kansha.alembic.admin:AlembicUpgradeCommand
      create-index = kansha.batch.create_index:ReIndex
      save-config = kansha.batch.save_config:SaveConfig
      create-demo = kansha.batch.create_demo:CreateDemo

      [kansha.services]
      authentication = kansha.services.authentication_repository:AuthenticationsRepository
      mail_sender = kansha.services.mail:MailSender
      assets_manager = kansha.services.simpleassetsmanager.simpleassetsmanager:SimpleAssetsManager

      [kansha.authentication]
      dblogin = kansha.authentication.database.forms:Login
      oauthlogin = kansha.authentication.oauth.forms:Login
      ldaplogin = kansha.authentication.ldap.forms:Login

      [kansha.card.extensions]
      labels = kansha.card_addons.label.comp:CardLabels
      description = kansha.card_addons.description.comp:CardDescription
      checklists = kansha.card_addons.checklist.comp:Checklists
      gallery = kansha.card_addons.gallery.comp:Gallery
      comments = kansha.card_addons.comment.comp:Comments
      due_date = kansha.card_addons.due_date.comp:DueDate
      votes = kansha.card_addons.vote.comp:Votes
      weight = kansha.card_addons.weight:CardWeightEditor
      members = kansha.card_addons.members:CardMembers

      [nagare.applications]
      kansha = kansha.app:app

      [search.engines]
      dummy = kansha.services.search.dummyengine:DummySearchEngine
      sqlite = kansha.services.search.sqliteengine:SQLiteFTSEngine
      elastic = kansha.services.search.elasticengine:ElasticSearchEngine
      """
)
