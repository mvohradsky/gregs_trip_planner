from odoo import models, fields, api

class ServiceTrip(models.Model):
    _name = 'gregs.service_trip'
    _description = 'Service Trip'

    name = fields.Char(string='Název výjezdu', required=True)
    task_id = fields.Many2one('project.task', string='Úkol', required=True)
    start_datetime = fields.Datetime(string='Začátek výjezdu', required=True)
    end_datetime = fields.Datetime(string='Konec výjezdu', required=True)
    team_id = fields.Many2one('gregs.service_team', string='Tým techniků', required=True)
    responsible_user_id = fields.Many2one('res.users', string='Odpovědný technik', required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vozidlo', required=True)
    contact_person = fields.Char(string='Kontaktní osoba')
    contact_phone = fields.Char(string='Telefon kontaktu')
    location_address = fields.Char(string='Adresa/GPS místa zásahu')

    state = fields.Selection([
        ('planned', 'Naplánováno'),
        ('in_progress', 'Probíhá'),
        ('done', 'Hotovo'),
    ], string='Stav výjezdu', default='planned')

    # Metody pro změnu stavu výjezdu
    def set_state_planned(self):
        self.state = 'planned'

    def set_state_in_progress(self):
        self.state = 'in_progress'

    def set_state_done(self):
        self.state = 'done'

    # Metoda pro vytvoření výjezdu z úkolu (např. při drag&drop z kalendáře)
    @api.model
    def create_trip_from_task(self, task_id, start_datetime):
        task = self.env['project.task'].browse(task_id)
        if task:
            trip = self.create({
                'name': task.name,
                'task_id': task.id,
                'start_datetime': start_datetime,
                'end_datetime': start_datetime,
                'responsible_user_id': task.user_id.id,
                'contact_person': task.partner_id.name,
                'contact_phone': task.partner_id.phone,
                'location_address': task.partner_id.contact_address,
            })
            return trip.id
        return False