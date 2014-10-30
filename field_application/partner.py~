# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

class partner_fiscal_application(osv.osv):
    
    _inherit = "res.partner"
    
    _columns = {
            'application': fields.selection([
                                      ('final_customer','Final Customer'),
                                      ('resale','Resale'),
                                      ],'Application', readonly=False, required=False),
                }

    _defaults = {'application':'final_customer',
                 }



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
