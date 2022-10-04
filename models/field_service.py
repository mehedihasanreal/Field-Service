from odoo import api, fields, models, _


class FieldService(models.Model):
    _name = 'field.service'
    _description = 'Field Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "order_no"

    order_no = fields.Char(string='Order No.', required=True, readonly=True, tracking=True,
                           default=lambda self: _('New'))
    order_date = fields.Date(string="Order Date", default=fields.Date.context_today)
    branch = fields.Selection([('mirpur', 'Mirpur'), ('uttara', 'Uttara')], string="Branch", tracking=True)
    dealer = fields.Selection([('dell', 'Dell'), ('hp', 'HP'), ('smart', 'Smart')], string="Dealer/Retailer")
    communication_media = fields.Selection([('call', 'Call'), ('email', 'Email')], string="Communication Media")
    service_type = fields.Selection([('repair', 'Repair'), ('maintenance', 'Maintenance')], string="Service Type")
    imei = fields.Char(string="IMEI/Serial No")
    invoice_no = fields.Char(string="Invoice No")
    invoice_attachment = fields.Image(string="Invoice Attachment")
    product_id = fields.Many2one('product.product', required=True)
    customer_id = fields.Many2one('res.partner', required=True)
    outlet = fields.Char(string="Outlet")

    @api.model
    def create(self, vals):
        if vals.get('order_no', _('New')) == _('New'):
            vals['order_no'] = self.env['ir.sequence'].next_by_code('field.service') or _('New')
        res = super(FieldService, self).create(vals)
        return res

    def actions_test(self):
        return