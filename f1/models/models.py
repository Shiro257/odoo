# -*- coding: utf-8 -*-

from odoo import models, fields, api



class player(models.Model):
     _name = 'f1.player'

     Nombre = fields.Char()

class f1(models.Model):
     _name = 'f1.f1'

     Equipos = fields.Many2many('f1.equipo', relation='equipo_f1')
     Motores = fields.Many2many('f1.motores', relation='motores_f1')
     #Pilotos = fields.Many2many('f1.pilotos', relation='f1_pilotos')


class equipo(models.Model):
     _name= 'f1.equipo'

     Nombre = fields.Char()
     Pais = fields.Char()
     Director = fields.Char()
     f1 = fields.Many2many('f1.f1', relation='f1_Equipos')

class motores(models.Model):
     _name = 'f1.motores'

     Fabricante = fields.Char()
     Potencia = fields.Char()
     f1 = fields.Many2many('f1.f1', relation='f1_Motores')

class pilotos(models.Model):
     _name = 'f1.pilotos'

     Nombre = fields.Char()
     Edad = fields.Integer()
     Pais = fields.Char()
     FechaNacimiento = fields.Date()
     Poles = fields.Integer()
     Victorias = fields.Integer()
     Titulos = fields.Integer()
     #f1 = fields.Many2many('f1.f1', relation='f1_Pilotos')
