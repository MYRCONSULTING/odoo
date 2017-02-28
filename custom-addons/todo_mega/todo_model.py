#-*- coding: utf-8 -*-
from openerp import models, fields, api

class SurveySurvey(models.Model):
    _inherit = ['survey.survey']
    x_product_ids = fields.Many2many('product.product',
                                         string='Survey')
    
class ProjectProject(models.Model):
    _inherit = ['project.project']
    x_survey_id = fields.Many2one('survey.survey',string='Encuesta')
    
class ProjectTask(models.Model):
    _inherit = ['project.task']
    x_survey_id = fields.Many2one('survey.survey',string='Encuesta')
    x_survey_user_input_id = fields.Many2one('survey.user_input',string='Respuesta')
    
class SurveyUserInput(models.Model):
    _inherit = ['survey.user_input']
    x_product_ids = fields.Many2one('product.product')
    x_project_task_ids = fields.Many2one('project.task')
    