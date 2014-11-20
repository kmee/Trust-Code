# -*- coding: utf-8 -*-

from openerp.osv import orm, fields

class sale_contact(orm.Model):
    _inherit = 'sale.order'
    
    _columns = {
              'partner_contact_id': fields.many2one('res.partner', 
                                                     'partner_id',
                                                     domain="[('parent_id','=',partner_id)]",
                                                     readonly=True,
                                                     required=True,
                                                     states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                                     help="Insert here the comercial contact."),
                }