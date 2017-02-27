#-*- coding: utf-8 -*-
from openerp import models, fields, api

class SurveySurvey(models.Model):
    _inherit = ['survey.survey']
    x_product_ids = fields.Many2many('product.product',
                                         string='Survey')
    

class SurveyUserInput(models.Model):
    _inherit = ['survey.user_input']
    x_product_ids = fields.Many2one('product.product')
    

class ProjectProject(models.Model):
    _inherit = ['project.project']
    x_survey_id = fields.Many2one('survey.survey',string='Encuesta')
    