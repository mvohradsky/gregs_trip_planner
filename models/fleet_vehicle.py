from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'
    is_service_vehicle = fields.Boolean('Service Vehicle')