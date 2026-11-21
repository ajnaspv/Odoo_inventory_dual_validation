from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    state = fields.Selection(selection_add=[('to_approve','To Approve')])

    def button_validate(self):
        print(self)
        if (self.env.user.has_group('inventory_dual_validation.internal_transfer_staff_user') and self.picking_type_code == 'internal'):
            self.action_confirm()
            self.state = "to_approve"
        else:
            return super().button_validate()

    def button_approve(self):
        if (self.env.user.has_group('inventory_dual_validation.internal_transfer_approver')):
            self.button_validate()
        else:
            self.state = "to_approve"