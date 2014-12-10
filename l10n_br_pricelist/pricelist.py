# -*- coding: utf-8 -*-

import time
from openerp.osv import orm, fields

class l10n_br_account_tax(orm.Model):
    _inherit = 'account.tax'
    
    _columns = {
              'tax_price': fields.boolean('Add_Tax_Price',)
                }

class l10n_br_sale_order_line (orm.Model):
    _inherit = 'sale.order.line'
    
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        
        retorno = super(l10n_br_sale_order_line, self).product_id_change(cr, uid, ids, pricelist,
                        product, qty, uom, qty_uos, uos, name, partner_id, lang, update_tax, date_order,
                        packaging, fiscal_position, flag, context)
        
        return retorno
    
    
class l10n_br_pricelist (orm.Model):
    _inherit = 'product.pricelist'
    
    def price_get_multi(self, cr, uid, pricelist_ids, products_by_qty_by_partner, context=None):
        """multi products 'price_get'.
           @param pricelist_ids:
           @param products_by_qty:
           @param partner:
           @param context: {
             'date': Date of the pricelist (%Y-%m-%d),}
           @return: a dict of dict with product_id as key and a dict 'price by pricelist' as value
        """
        res = super(l10n_br_pricelist, self).price_get_multi(cr, uid, ids, pricelist_ids, products_by_qty_by_partner, context)
        return res
#     
    
    def price_get(self, cr, uid, ids, prod_id, qty, partner=None, context=None):        
        res = super(l10n_br_pricelist, self).price_get(cr, uid, ids, prod_id, qty, partner, context)        
        return res
    
