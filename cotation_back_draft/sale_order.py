# -*- coding: utf-8 -*-

from openerp.osv import orm, fields

class sale_contact(orm.Model):
    _inherit = 'sale.order'
    
    def button_back_draft(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'draft'})
