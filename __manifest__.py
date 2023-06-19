{
	'name': 'Motorcycle Registry',
	'summary': 'Manage Registration of Motorcycles',
	'description': """Motorcycle Registry
			====================
			This Module is used to keep track of the Motorcycle
			 Registration and Ownership of each motorcycled
			 of the brand.""",
	'license': 'OPL-1',
	'author': 'cobr-odoo',
	'website': '16-motorcylce_registry',
	'category': 'Kawill/',
	'depends': ['base'],
        'data': [
            'security/motorcycle_groups.xml',
            'security/ir.model.access.csv','security/motorcycle_security.xml',
            'data/registry_data.xml',
            'views/motorcycle_menuitems.xml',
            'views/registry_views.xml'
		],
	'demo': [
		'demo/motorcycle_demo.xml'
	],
        'application': True,
}
