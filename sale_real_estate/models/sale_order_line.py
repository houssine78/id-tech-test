from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model_create_multi
    def create(self, vals_list):
        lines = super().create(vals_list)
        order_id = lines.order_id
        return order_id.compute_analytic_distribution(order_id.real_estate_project_id.id)

