from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'
    requires_trip = fields.Boolean('Requires Trip')