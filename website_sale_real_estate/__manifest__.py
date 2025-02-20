# Copyright 2025 Open Architects Consulting SRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Real estate project on E-Commerce",
    "summary": "Real estate feature on E-Commerce",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "author": "Open Architects Consulting SRL, Houssine Bakkali",
    "license": "AGPL-3",
    "depends": [
        "website_sale",
        "web"
    ],
    "data": [
        "templates/website_sale_templates.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'website_sale_real_estate/static/src/js/website_sale.js',
        ]
    },
    "installable": True,
}
