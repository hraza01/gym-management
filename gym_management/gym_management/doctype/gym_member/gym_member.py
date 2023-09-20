# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime as dt


class GymMember(Document):
    def get_full_name(self):
        """Returns the passenger's full name"""
        if not self.last_name:
            return self.first_name

        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        """Returns the age given the date of birth"""
        today = dt.date.today()
        dob = get_parsed_date(self.date_of_birth)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        return age

    def before_save(self):
        dob = get_parsed_date(self.date_of_birth)

        if dob.date() > dt.date.today():
            frappe.throw("Date of Birth cannot be greater than today.")

        self.full_name = self.get_full_name()
        self.age = self.get_age()

    def after_insert(self):
        create_user(self)


def get_parsed_date(date):
    return dt.datetime.strptime(date, "%Y-%m-%d")


def create_user(member):
    doc = frappe.db.exists("User", member.email)

    if doc:
        user = frappe.get_doc("User", member.email)
        user.append("roles", {"doctype": "Has Role", "role": "Gym Member"})
        user.save()

    else:
        user = frappe.get_doc(
            {
                "doctype": "User",
                "email": member.email,
                "first_name": member.first_name,
                "last_name": member.last_name,
            }
        )
        user.append("roles", {"doctype": "Has Role", "role": "Gym Member"})
        user.insert()
