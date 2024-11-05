# -*- coding: utf-8 -*-
# from odoo import http


# class MageIsland(http.Controller):
#     @http.route('/mage_island/mage_island', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mage_island/mage_island/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mage_island.listing', {
#             'root': '/mage_island/mage_island',
#             'objects': http.request.env['mage_island.mage_island'].search([]),
#         })

#     @http.route('/mage_island/mage_island/objects/<model("mage_island.mage_island"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mage_island.object', {
#             'object': obj
#         })

