#-*- coding: utf-8 -*-
from openerp import models, fields, api

class SurveySurvey(models.Model):
    _name = 'survey.survey'
    _inherit = ['survey.survey']
    product_ids = fields.Many2many('product.product',
                                         string='Survey')