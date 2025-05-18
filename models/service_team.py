from odoo import models, fields

class ServiceTeam(models.Model):
    _name = 'gregs.service_team'
    _description = 'Service Team'

    name = fields.Char(string='Název týmu', required=True)
    user_ids = fields.Many2many('res.users', string='Členové týmu', required=True)
