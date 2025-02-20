# Copyright 2025 Open Architects Consulting SRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, models
from odoo.tools.translate import _, LazyTranslate

_lt = LazyTranslate(__name__)

class Website(models.Model):
    _inherit = 'website'

    def _get_checkout_step_list(self):
        """ Return an ordered list of steps according to the current template rendered.

        :rtype: list
        :return: A list with the following structure:
            [
                [xmlid],
                {
                    'name': str,
                    'current_href': str,
                    'main_button': str,
                    'main_button_href': str,
                    'back_button': str,
                    'back_button_href': str
                }
            ]
        """
        self.ensure_one()
        is_extra_step_active = self.viewref('website_sale.extra_info').active
        redirect_to_sign_in = self.account_on_checkout == 'mandatory' and self.is_public_user()

        steps = [(['website_sale.cart'], {
            'name': _lt("Review Order"),
            'current_href': '/shop/cart',
            'main_button': _lt("Sign In") if redirect_to_sign_in else _lt("Real Estate Project"),
            'main_button_href': f'{"/web/login?redirect=" if redirect_to_sign_in else ""}/shop/real_estate_project',
            # 'main_button': _lt("Continue checkout"),
            # 'main_button_href': '/shop/checkout?try_skip_step=true',
            'back_button':  _lt("Continue shopping"),
            'back_button_href': '/shop',
        }), 
            (['website_sale_real_estate.real_estate_project'], {
                'name': _lt("Real Estate Project"),
                'current_href': '/shop/real_estate_project',
                'main_button': _lt("Continue checkout"),
                'main_button_href': '/shop/checkout?try_skip_step=true',
                'back_button':  _lt("Back to cart"),
                'back_button_href': '/shop/cart',
        }),
            (['website_sale.checkout', 'website_sale.address'], {
            'name': _lt("Delivery"),
            'current_href': '/shop/checkout',
            'main_button': _lt("Confirm"),
            'main_button_href': f'{"/shop/extra_info" if is_extra_step_active else "/shop/confirm_order"}',
            'back_button':  _lt("Real Estate Project"),
            'back_button_href': '/shop/real_estate_project',
        })]
        if is_extra_step_active:
            steps.append((['website_sale.extra_info'], {
                'name': _lt("Extra Info"),
                'current_href': '/shop/extra_info',
                'main_button': _lt("Continue checkout"),
                'main_button_href': '/shop/confirm_order',
                'back_button':  _lt("Back to delivery"),
                'back_button_href': '/shop/checkout',
            }))
        steps.append((['website_sale.payment'], {
            'name': _lt("Payment"),
            'current_href': '/shop/payment',
            'back_button':  _lt("Back to delivery"),
            'back_button_href': '/shop/checkout',
        }))
        return steps
