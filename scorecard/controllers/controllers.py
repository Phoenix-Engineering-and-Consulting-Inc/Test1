# -*- coding: utf-8 -*-
# from odoo import http


 class Scorecard(http.Controller):
     @http.route('/scorecard/scorecard/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/scorecard/scorecard/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('scorecard.listing', {
             'root': '/scorecard/scorecard',
             'objects': http.request.env['scorecard.scorecard'].search([]),
         })

     @http.route('/scorecard/scorecard/objects/<model("scorecard.scorecard"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('scorecard.object', {
             'object': obj
         })
