# -*- coding: utf-8 -*-
# Copyright 2016 Tecnativa <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from . import models
from odoo import api, SUPERUSER_ID

def create_code_equal_to_id(cr):
    """
    With this pre-init-hook we want to avoid error when creating the UNIQUE
    code constraint when the module is installed and before the post-init-hook
    is launched.
    """
    cr.execute('ALTER TABLE project_task '
               'ADD COLUMN code character varying;')
    cr.execute('UPDATE project_task '
               'SET code = id;')


