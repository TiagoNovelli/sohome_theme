{
    'name': 'Sohome Theme',
    'version': '18.1.0',
    'category': 'Themes/Backend',
    'summary': 'Tema premium corporativo — oliva · bege · dourado',
    'depends': ['web', 'web_responsive', 'web_pwa_customize'],
    'data': [
        'views/favicon.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'sohome_theme/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            'sohome_theme/static/src/scss/styles.scss',
        ],
        # Login page: loaded no contexto frontend (página /web/login)
        'web.assets_frontend': [
            'sohome_theme/static/src/scss/login.scss',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
