# -*- coding: utf-8 -*-
###############################################################################
#
#    Leewise Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Leewise Technologies(<https://www.leewise.in>)
#    Author: Leewise Techno Solutions (leewise@leewise.in)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': "Automatic Database Backup To Local Server, Remote Server,"
            "Google Drive, Dropbox, Onedrive, Nextcloud and Amazon S3 Leewise17",
    'version': '17.0.6.0.1',
    'category': 'Extra Tools',
    'summary': 'Leewise Database Backup, Automatic Backup, Database Backup, Automatic Backup,Database auto-backup, leewise backup'
               'google drive, dropbox, nextcloud, amazon S3, onedrive or '
               'remote server, Leewise17, Backup, Database, Leewise Apps',
    'description': 'Leewise Database Backup, Database Backup, Automatic Backup, automatic database backup, leewise17, leewise apps,backup, automatic backup,leewise17 automatic database backup,backup google drive,backup dropbox, backup nextcloud, backup amazon S3, backup onedrive',
    'author': "Leewise",
    'company': 'Leewise',
    'maintainer': 'Leewise',
    'website': "https://www.leewise.in",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'views/db_backup_configure_views.xml',
        'wizard/dropbox_auth_code_views.xml',
    ],
    'external_dependencies': {
        'python': ['dropbox', 'pyncclient', 'boto3', 'nextcloud-api-wrapper','paramiko']},
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
