{
    'name': 'Sohome Theme',
    'version': '1.0',
    'category': 'Themes/Backend',
    'depends': ['web'],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'sohome_theme/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            'sohome_theme/static/src/scss/styles.scss',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
