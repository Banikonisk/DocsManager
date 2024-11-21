from odoo import models, fields


class Document(models.Model):
    _name = 'documents.document'
    _description = 'Document'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    user_id = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    employee_ids = fields.Many2many('hr.employee', string='Responsible Employees')
