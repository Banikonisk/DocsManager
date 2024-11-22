{
    'name': 'Documents & Books Management Module',
    'version': '1.0',
    'author': 'Karolis',
    'category': 'Extra Tools',
    'summary': 'Documents & Books Management Tool',
    'description': 'Module to manage documents and books',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_views.xml'
    ],
    'license': 'LGPL-3',
    'installable': True
}
