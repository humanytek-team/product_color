# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models


class ProductColor(models.Model):
    _name = 'product.color'

    name = fields.Char('Color Name', required=True)
    color = fields.Char('Color', help='Choose the color', default='#FFFFFF')
    product_ids = fields.One2many(
        'product.template',
        'product_color_id',
        string='Colors Products',
    )
    products_count = fields.Integer(
        string='Number of products',
        compute='_get_products_count',
    )

    @api.one
    @api.depends('product_ids')
    def _get_products_count(self):
        self.products_count = len(self.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_color_id = fields.Many2one(
        'product.color',
        string='Color',
        help='Select a color for this product'
    )
