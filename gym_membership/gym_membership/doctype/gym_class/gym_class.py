# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from gym_membership.utils.helpers import get_end_time


class GymClass(Document):
    def before_save(self):
        end_time = get_end_time(self.start_time, self.duration)
        self.end_time = str(end_time)
