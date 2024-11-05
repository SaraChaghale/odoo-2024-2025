# -*- coding: utf-8 -*-
from odoo import models, fields

class Player(models.Model):
    _name = 'mage_island.player'
    _description = 'Player'

    name = fields.Char(string="Nombre", required=True, help="Introduce tu nombre")
    photo = fields.Image(max_width=200, max_height=200)
    last_login = fields.Datetime()
    mage_ids = fields.One2many('mage_island.mage', 'player_id', string="Mages")

class Island(models.Model):
    _name = 'mage_island.island'
    _description = 'Island'

    name = fields.Char(string="Nombre", required=True)
    mage_ids = fields.One2many('mage_island.mage', 'island_id', string="Mages")
    object_ids = fields.One2many('mage_island.object', 'island_id', string="Objects")

class Mage(models.Model):
    _name = 'mage_island.mage'
    _description = 'Mage'

    name = fields.Char(default="Mago", required=True)
    live = fields.Float(default=50)
    power = fields.Float(default=100)
    defense = fields.Integer(default=50)
    island_id = fields.Many2one('mage_island.island', string="Island")
    player_id = fields.Many2one('mage_island.player', string="Player")
    object_id = fields.Many2one('mage_island.object', string="Object")

class Object(models.Model):
    _name = 'mage_island.object'
    _description = 'Object'

    name = fields.Char(string="Objeto", required=True)
    quantity = fields.Integer(string="Cantidad")
    island_id = fields.Many2one('mage_island.island', string="Island")
    mage_id = fields.Many2one('mage_island.mage', string="Mage")
