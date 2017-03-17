# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'To-Do Mega',
    'author' : 'Megatienda',
    'depends' : ['project','survey','contacts','purchase'],
    'category' : 'MegaTienda',
    'application' : True,
    'website': 'http://www.megatienda.com.pe',
    'data': [
        'todo_view_survey.xml',
        'todo_view_project_project.xml',
        'todo_view_project_task.xml',
        'todo_view_survey_user_input.xml',
        'security/todo_access_rules.xml'
    ],
    'installable'    :   True,
    'auto_install'  :   True,
    'active'    :   True
}