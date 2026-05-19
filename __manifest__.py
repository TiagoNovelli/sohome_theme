{
    'name': 'Sohome Theme',
    'version': '18.1.1',
    'category': 'Themes/Backend',
    'summary': 'Paleta de cores SOHOME sobre o tema padrão do Odoo 18',
    'depends': ['web'],
    'data': [
        'views/favicon.xml',
    ],
    'assets': {
        # Injeta as variáveis ANTES das do Odoo — propaga para todos os componentes
        'web._assets_primary_variables': [
            ('prepend', 'sohome_theme/static/src/scss/primary_variables.scss'),
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
