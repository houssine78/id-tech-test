from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    real_estate_project_id = fields.Many2one(
        'real.estate.project',
        copy=False
    )
    real_estate_project_state = fields.Selection(
        string="Real estate project state",
        related="real_estate_project_id.state"
    )

    def compute_analytic_distribution(self, real_estate_project_id):
        realEstateProject = self.env['real.estate.project']
        project = realEstateProject.browse(real_estate_project_id)

        old_analytic_account = (self.real_estate_project_id
                                and self.real_estate_project_id.account_analytic_id
                                or None)

        new_analytic_account = project.account_analytic_id

        for line in self.order_line:
            analytic_distribution = line.analytic_distribution or {}
            if old_analytic_account and str(old_analytic_account.id) in analytic_distribution.keys():
                del analytic_distribution[str(old_analytic_account.id)]
            if new_analytic_account:
                analytic_distribution.update({
                    str(new_analytic_account.id): 100
                })
            line.analytic_distribution = analytic_distribution

        return self.order_line
    
    def write(self, vals):
        for order in self:
            if 'real_estate_project_id' in vals:
                real_estate_project_id = vals['real_estate_project_id']
                order.compute_analytic_distribution(real_estate_project_id)
        return super().write(vals)
