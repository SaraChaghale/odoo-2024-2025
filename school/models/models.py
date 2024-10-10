# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(string='Name', required=True)
    # value = fields.Integer(string='Value')
    # value2 = fields.Float(compute="_value_pc", store=True, string='Value 2')
    # description = fields.Text(string='Description')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100



