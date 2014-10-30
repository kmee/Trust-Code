# -*- coding: utf-8 -*-

from openerp.osv import orm, fields
from openerp.tools.translate import _

class sale_product_configurator(orm.Model):
    _inherit = 'sale.order'
    
    _columns = {
            'resin': fields.selection([
                                      ('isophthalic','Isophthalic'),
                                      ('off-shore','Off-Shore'),
                                      ('orthophthalic','Orthophthalic'), 
                                      ('phynolic','Phynolic'),
                                      ('vinyl ester','Vinyl Ester')],
                                      'Resin', readonly=False, select=True, required=True),
            'fixation': fields.selection([
                                          ('stainless steel 304','Stainless Steel 304'),
                                          ('stainless steel 316','Stainless Steel 316'),
                                          ('stainless steel 316L','Stainless Steel 316L'),
                                          ],'Fixation', readonly=False, select=True, required=True),
            'color': fields.selection([
                                      ('yellow safety','Yellow Safety'),
                                      ('gray','Gray'),
                                      ('yellow safety/gray','Yellow Safety/Gray'),
                                      ('green','Green'),
                                      ('write','Write'),
                                      ('special','Special'),
                                      ],'Color', readonly=False, select=True, required=True),
            'special color': fields.char ('Special Color', size=20, help='Insert here the special color.'),
                }
    
    _defaults = {
                 'resin': 'isophthalic',
                 'fixation': 'stainless steel 304',
                 'color': 'yellow sagety/gray',
                 }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
