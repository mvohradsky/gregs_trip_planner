{
    'name': 'Gregs Trip Planner',
    'version': '1.3',
    'category': 'Services',
    'summary': 'Plánování a správa servisních výjezdů',
    'description': """
        Modul umožňuje efektivní plánování a řízení servisních a montážních výjezdů.
        Zahrnuje kalendář, drag-and-drop plánování, týmovou správu a mobilní rozhraní pro techniky.
    """,
    'author': 'Gregs s.r.o.',
    'website': 'https://www.gregs.cz',
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
            'gregs_trip_planner/static/src/js/trip_calendar.js'
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}