#-*- coding: utf-8 -*-
from openerp import models, fields, api

class SurveySurvey(models.Model):
    _name = 'survey.survey'
    _inherit = ['survey.survey']
    x_many_product_id = fields.Many2many('product.product', 'Productos')