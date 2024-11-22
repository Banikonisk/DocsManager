{
    'name': 'Documents & Books Management Module',
    'version': '1.0',
    'author': 'Karolis',
    'category': 'Extra Tools',
    'summary': 'Documents & Books Management Tool',
    'description': 'Module to manage documents and books',
    'depends': ['base', 'hr'],
    'data': [
        'security/docs_information_security.xml',
        'security/ir.model.access.csv',
        'wizard/document_filter_wizard_view.xml',
        'views/document_views.xml',
        'report/report_document_template.xml',
        'report/report_document.xml'
    ],
    'license': 'LGPL-3',
    'installable': True
}
