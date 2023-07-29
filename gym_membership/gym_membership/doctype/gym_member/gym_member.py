# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import datetime as dt

class GymMember(Document):

    def get_full_name(self):
        """Returns the passenger's full name"""
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        """Returns the age given the date of birth"""
        today = dt.date.today()
        parsed_dob = dt.datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age = today.year - parsed_dob.year - ((today.month, today.day) < (parsed_dob.month, parsed_dob.day))

        return age

    def before_save(self):
        self.full_name = self.get_full_name()
        self.age = self.get_age()
