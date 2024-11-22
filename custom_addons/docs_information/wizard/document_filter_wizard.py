from odoo import models, fields, exceptions

class DocumentFilterWizard(models.TransientModel):
    _name = 'document.filter.wizard'
    _description = 'Document Filter Wizard'

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('hr.employee', string='Employee')

    def action_print_report(self):
        domain = []
        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))
        if self.employee_id:
            domain.append(('employee_ids', 'in', self.employee_id.ids))

        documents = self.env['documents.document'].search(domain)
        if not documents:
            raise exceptions.UserError("No documents found for the selected criteria.")
        return self.env.ref('docs_information.action_report_documents').report_action(documents)