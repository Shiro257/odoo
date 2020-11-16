# -*- coding: utf-8 -*-

from odoo import models, fields, api

class universidad(models.Model):
     _name = 'universidad.universidad'
     _description = 'universidad.universidad'

     name = fields.Char()
     num = fields.Integer()
     numFloat = fields.Float()
     fecha = fields.Date()
     photo = fields.Image(max_width=200)
     prioridad = fields.Selection([('1', 'mu bajo'), ('2', 'bajo'), ('3', 'normal'), ('4', 'alto'), ('5', 'mu alto')])
     profesores = fields.One2many('universidad.universidad2', 'prof')
     clases = fields.Many2many('universidad.universidad2', relation='universidad2_clases')

class universidad2(models.Model):
    _name = 'universidad.universidad2'

    name = fields.Char()
    fechaTiempo = fields.Datetime()
    photo = fields.Image(max_width=200)
    prioridad = fields.Selection([('1', 'mu bajo'), ('2', 'bajo'), ('3', 'normal'), ('4', 'alto'), ('5', 'mu alto')])
    prof = fields.Many2one('universidad.universidad')
    clases = fields.Many2many('universidad.universidad', relation='universidad2_clases')
