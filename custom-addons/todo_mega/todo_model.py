#-*- coding: utf-8 -*-
from openerp import models, fields, api

class SurveySurvey(models.Model):
    _inherit = ['survey.survey']
    x_product_ids = fields.Many2many('product.product',
                                         string='Survey')