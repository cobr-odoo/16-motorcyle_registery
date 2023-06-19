from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Registry(models.Model):
	_name = "motorcycle.registry"
	_description = "Registry for a motorcycle"
	# _sql_constraints = [
    #     ('vin_unique', 'UNIQUE(vin)', 'Another registration for this VIN Number already exists.')
    # ]

	registry_number = fields.Char(string="Registry Number", required=True,
			       default="MRN0000", copy=False, readonly=True)


	vin = fields.Char(string='VIN', required=True)
	first_name = fields.Char(string='First Name',required=True)
	last_name = fields.Char(string='Last Name', required=True)
	picture = fields.Image(string='Photograph')
	current_mileage = fields.Float(string="Current Mileage")
	license_plate = fields.Char(string='License Plate Number')
	certificate_title = fields.Binary(string='Certificate of Title')
	register_date = fields.Date(string='Registration Date')

	@api.model_create_multi
	def create(self, vals_list):
		for vals in vals_list:
			if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
				vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
		return super().create(vals_list)
	
	@api.constrains('vin')
	def _check_vin(self):
		pattern = r'^[A-Z]{4}\d{2}(d{2}|[A-Z]{2})\d{6}'
		for registry in self:
			if not (re.match(pattern, registry.vin)):
				raise ValidationError("Invalid VIN")
			
	@api.constrains('vin')
	def _check_unique_vin(self):
		for record in self:
			existing_record = self.search([('vin', '=', record.vin)])
			if len(existing_record) > 1:
				raise ValidationError('Another registration for this VIN Number already exists.')

	 
	@api.constrains('license_plate')
	def _check_license_plate(self):
		pattern = r'^[A-Z]{1,4}\d{1,3}(?:[A-Z]{1,2})'
		for registry in self:
			if not (re.match(pattern, registry.vin)):
				raise ValidationError("Invalid License Plate")