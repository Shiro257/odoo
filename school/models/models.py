# -*- coding: utf-8 -*-

from odoo import models, fields, api


class couse(models.Model):
    _name = 'school.course'
    _description = 'courses'

    name = fields.Char(string="Tasca",required=True)
    date = fields.Datetime()
    done = fields.Boolean()
    photo = fields.Image(max_width=200)
    priority = fields.Selection([('1','Low'),('2','Normal'),('3','High')])