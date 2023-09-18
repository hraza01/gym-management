# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymTrainer(Document):

    def get_full_name(self):
        """Returns the passenger's full name"""
        return f'{self.first_name} {self.last_name}'

    def before_save(self):

        self.full_name = self.get_full_name()
