# -*- coding: utf-8 -*-

from odoo import models, fields, api



class custom_calendar_event(models.Model):

    # This model extends the calendar.event

    _description = 'Custom calendar event model'
    _inherit = ['calendar.event']

    is_validated = fields.Boolean(default=False,string="Is validated", help="If the meeting is validated", translate=True)
