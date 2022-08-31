# -*- coding: utf-8 -*-

from odoo import models, fields, api

VALIDATION_SELECTION = (
    ('validated', 'Is validated'),
    ('not_validated', 'Is not validated'),
)

class custom_calendar_event(models.Model):

    # This model extends the calendar.event

    _description = 'Custom calendar event model'
    _inherit = ['calendar.event']

    #is_validated = fields.Boolean(default=False,string="Is validated", help="If the meeting is validated", translate=True)
    validation = fields.Selection(
        [('true', 'Yes'),
         ('false', 'No'),
        ],
        'Validated', default='false', required=True,
        help="If the meeting is validated")
    """
    validation = fields.Selection(
        string="Validation status",
        selection=VALIDATION_SELECTION,   
        default='not_validated')
    """
    

