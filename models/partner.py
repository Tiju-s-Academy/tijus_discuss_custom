from odoo import models,fields,api

class ResPartner(models.Model):
    _inherit = "res.partner"

    has_user = fields.Boolean(compute="_compute_has_user", store=True)

    @api.depends('user_ids')
    def _compute_has_user(self):
        for record in self:
            record.has_user = len(record.user_ids) > 0