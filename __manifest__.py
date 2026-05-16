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
        # Cada arquivo listado individualmente — @import é proibido no Odoo
        'web.assets_backend': [
            'sohome_theme/static/src/scss/base.scss',
            'sohome_theme/static/src/scss/navigation.scss',
            'sohome_theme/static/src/scss/components.scss',
            'sohome_theme/static/src/scss/tables.scss',
            'sohome_theme/static/src/scss/kanban.scss',
            'sohome_theme/static/src/scss/dashboard.scss',
            'sohome_theme/static/src/scss/home_menu.scss',
            'sohome_theme/static/src/scss/animations.scss',
        ],
        'web.assets_frontend': [
            'sohome_theme/static/src/scss/login.scss',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
