# -*- coding: utf-8 -*-

from openerp.osv import orm, fields

class AccountTax(orm.Model):
    _inherit = 'account.tax'
    
    _columns = {
        'tax_in_price': fields.boolean('Add Tax in Price', help='Select this field for add this tax in sale markup when used pricelists')
        }

class SaleOrderLine(orm.Model):
    _inherit = 'sale.order.line'
    
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
                          uom=False, qty_uos=0, uos=False, name='',
                          partner_id=False, lang=False, update_tax=True,
                          date_order=False, packaging=False,
                          fiscal_position=False, flag=False, context=None):

        result = super(SaleOrderLine, self).product_id_change(
            cr, uid, ids, pricelist, product, qty, uom, qty_uos, uos, name,
            partner_id, lang, update_tax, date_order, packaging,
            fiscal_position, flag, context)

        if result['value'].has_key('tax_id'):
            account_tax_obj = self.pool.get('account.tax')
            amount = 0
            for tax in account_tax_obj.browse(cr, uid, result['value']['tax_id']):
                if tax.tax_in_price:
                    amount += tax.amount
            result['value']['price_unit'] = result['value']['price_unit'] / (1 - amount)
        return result