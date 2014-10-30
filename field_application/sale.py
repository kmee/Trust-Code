# -*- coding: utf-8 -*-

from openerp.osv import orm, fields
from openerp.tools.translate import _

class sale_fiscal_application(orm.Model):
    _inherit = 'sale.order'
    
    _columns = {
            'application': fields.selection([
                                      ('final_customer','final_customer'),
                                      ('resale','Resale'),
                                      ],'Application', readonly=False, select=True, required=True),
                }

    def onchange_partner_id(self, cr, uid, ids, partner_id, context=None):
        
        result = {'value': {}}
        
        if not context:
            context = {}

        if not partner_id:
            result['value']['application'] = 'final_customer'
            return result
        
        partner_obj = self.pool.get('res.partner')
        partner_data  = partner_obj.browse(cr, uid, partner_id, context=context).application

        result['value']['application'] = partner_data
        
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
