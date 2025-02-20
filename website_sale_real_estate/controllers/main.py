import logging
from datetime import datetime

from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class WebsiteSale(WebsiteSale):

    @http.route(['/shop/real_estate_project'], type='http', auth="public", website=True, sitemap=False)
    def real_estate_project(self, **kwargs):
        # Check that cart is valid
        website_sale_order = request.website.sale_get_order()
        if not website_sale_order:
            return request.redirect('/shop')

        values = {
            'errors': [],
            'website_sale_order': website_sale_order,
            'real_estate_projects': request.env['real.estate.project'].search([]),
            'real_estate_project_id': website_sale_order.real_estate_project_id.id,
        }

        return request.render(
            'website_sale_real_estate.real_estate_project', values)

    @http.route(
        ["/shop/update_project"],
        type="json",
        auth="public",
        methods=["POST"],
        website=True,
    )
    def update_project(self, selected_project_id, **kw):
        website_sale_order = request.website.sale_get_order()
        project_obj = http.request.env["real.estate.project"]

        project = project_obj.sudo().browse(int(selected_project_id))
        website_sale_order.real_estate_project_id = project

        return True
