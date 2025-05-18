
{
    'name': 'Gregs Trip Planner',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Service trips and scheduling for Gregs',
    'depends': ['project', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_views.xml',
        'views/service_trip_views.xml',
        'views/service_team_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/trip_calendar_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            '/gregs_trip_planner/static/src/js/trip_calendar.js'
        ]
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
