from odoo import models, fields


class CostumModel(models.Model):
	#nama tabel db
	_name = 'custom.model'
	#fields table
	name    = fields.Char(String ='nama')
	age     = fields.Integer('Umur mu')
	address = fields.Text(String='address')   
	gender  = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')	