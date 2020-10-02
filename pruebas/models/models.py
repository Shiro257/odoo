# -*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
    _name = 'school.course'
    _description = 'courses'

    name = fields.Char()
