from odoo import fields, models


class RealEstateProject(models.Model):
    _name = 'real.estate.project'
    _description = "Real Estate Project"

    name = fields.Char(
        required=True,
        copy=False,
    )
    description = fields.Text()
    account_analytic_id = fields.Many2one(
        'account.analytic.account',
        required=True,
        copy=False
    )
    state = fields.Selection([
        ('planned', "Planned"),
        ('ongoing', "Ongoing"),
        ('completed', "Completed"),
        ],
        string="Status",
        readonly=True,
        copy=False,
        default="planned",
    )
    active = fields.Boolean(
        'Active', default=True,
        help="If unchecked, it will allow you to hide the project without removing it.")

    def action_plan(self):
        self.state = 'planned'

    def action_ongoing(self):
        self.state = 'ongoing'

    def action_finish(self):
        self.state = 'completed'
