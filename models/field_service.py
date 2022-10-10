from odoo import api, fields, models, _
from datetime import date


class FieldService(models.Model):
    _name = 'field.service'
    _description = 'Field Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "order_no"

    order_no = fields.Char(string='Order No.', required=True, readonly=True, tracking=True,
                           default=lambda self: _('New'))
    order_date = fields.Date(string="Order Date", default=fields.Date.context_today)
    branch = fields.Selection([('mirpur', 'Mirpur'), ('uttara', 'Uttara')], string="Branch", tracking=True)
    retailer = fields.Many2one('res.partner.category', string="Dealer/Retailer")
    communication_media = fields.Selection([('call', 'Call'), ('email', 'Email')], string="Communication Media")
    service_type = fields.Selection([('repair', 'Repair'), ('maintenance', 'Maintenance')], string="Service Type")
    serial_no = fields.Many2one('field.service.data', string="IMEI/Serial No")
    invoice_no = fields.Char(related='serial_no.invoice_no', string="Invoice No")
    invoice_attachment = fields.Image(string="Invoice Attachment")
    product_id = fields.Many2one(related='serial_no.product_id', string="Product")
    customer_id = fields.Many2one(related='serial_no.customer_id', string="Customer")
    pop = fields.Date(related='serial_no.pop', string="POP Date")
    warranty_status = fields.Selection(related='serial_no.warranty_status', string="Warranty Status")
    warranty_expiry_date_l = fields.Date(related='serial_no.warranty_expiry_date_l', string="Warranty Expiry Date(L)")
    warranty_expiry_date_p = fields.Date(related='serial_no.warranty_expiry_date_p', string="Warranty Expiry Date(p)")
    guaranty_expiry_date = fields.Date(related='serial_no.guaranty_expiry_date', string="Guaranty Expiry Date")
    warranty_void_reason = fields.Selection([('warranty', 'Warranty'), ('guaranty', 'Guaranty'), ('repair', 'Repair'),
                                             ('maintenance', 'Maintenance')], string="Warranty Void Reason", readonly=False)
    department = fields.Selection([('dell', 'Dell'), ('hp', 'HP'), ('smart', 'Smart')], string="Department")
    priority_level = fields.Selection([('low', 'Low'), ('mid', 'Mid'), ('high', 'High'), ('very high', 'Very High'),
                                       ('vip', 'Vip')], string="Priority Level")
    possible_delivery_date = fields.Date(string="Possible Delivery Date")
    customer_remark = fields.Text(string="Customer Remark")
    remark = fields.Text(string="Remark")
    repair_status = fields.Selection([('repaired', 'Repaired'), ('not-repaired', 'Not-Repaired'),
                                      ('repairing', 'Repairing')], string="Repair Status")
    product_receive_date = fields.Date(string="Product Receive Date")
    delivery_date = fields.Date(string="Delivery Date")
    item_receive_branch = fields.Selection([('dhaka', 'Dhaka'), ('chittagong', 'Chittagong'), ('khulna', 'Khulna')],
                                           string="Item Receive Branch")
    item_receive_status = fields.Selection([('received', 'Received'), ('not-received', 'Not- Received')],
                                           string="Item Receive Status")
    is_receive_branch = fields.Boolean(string="Is Receive From?")
    is_so_transfer = fields.Boolean(string="Is SO Transfer?")
    is_sms = fields.Boolean(string="Is SMS?")

    @api.model
    def create(self, vals):
        if vals.get('order_no', _('New')) == _('New'):
            vals['order_no'] = self.env['ir.sequence'].next_by_code('field.service') or _('New')
        res = super(FieldService, self).create(vals)
        return res

    def actions_test(self):
        return
