# Copyright 2025 Open Architects Consulting SRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Real estate project on sales",
    "summary": "Real estate feature on sale order",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "author": "Open Architects Consulting SRL, Houssine Bakkali",
    "license": "AGPL-3",
    "depends": [
        "sale_management",
        "sale",
        "analytic"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_views.xml",
        "views/real_estate_project_views.xml"
    ],
    "installable": True,
}
