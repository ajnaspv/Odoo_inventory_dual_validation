from odoo import fields, models

class HotelGuestResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Hotel Guest Res Partner'

    is_hotel_guest = fields.Boolean(string='Is Hotel Guest', default=False)