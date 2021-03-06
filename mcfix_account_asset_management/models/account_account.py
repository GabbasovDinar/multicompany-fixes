# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, _
from odoo.exceptions import ValidationError


class AccountAccount(models.Model):
    _inherit = 'account.account'

    @api.constrains('company_id', 'asset_profile_id')
    def _check_company_id_asset_profile_id(self):
        for rec in self.sudo():
            if not rec.asset_profile_id.check_company(
                    rec.company_id
            ):
                raise ValidationError(
                    _('The Company in the Account and in '
                      'Account Asset profile ust be the same.'))
