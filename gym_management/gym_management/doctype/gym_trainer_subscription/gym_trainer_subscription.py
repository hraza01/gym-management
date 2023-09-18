# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymTrainerSubscription(Document):

    def before_save(self):
        exists = frappe.db.exists(
            'Gym Trainer Subscription',
            {
                'member_id': self.member_id,
                'docstatus': 1,
                'end_date': ('>', self.end_date),
            },
        )

        if exists:
            frappe.throw('There is an active membership for this member')
