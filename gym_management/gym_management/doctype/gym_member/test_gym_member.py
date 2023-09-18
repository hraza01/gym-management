# Copyright (c) 2023, Hasan Raza and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
import datetime as dt


class TestGymMember(FrappeTestCase):
    def test_fullname_is_set_automatically(self):
        test_member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "Tony",
            "last_name": "Smith",
            "date_of_birth": "1995-06-26",
            "email": "tony.smith@example.com",
            "phone": "9901234123"
        }).insert()

        self.assertEqual(test_member.full_name, "Tony Smith")

    def test_fullname_is_set_correctly_if_no_last_name(self):
        test_member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "Tony",
            "date_of_birth": "1995-06-26",
            "email": "tony.smith@example.com",
            "phone": "9901234123"
        }).insert()

        self.assertEqual(test_member.full_name, "Tony")

    def test_age_is_set_automatically(self):
        test_member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "Tony",
            "last_name": "Smith",
            "date_of_birth": "1995-06-26",
            "email": "tony.smith@example.com",
            "phone": "9901234123"
        }).insert()

        self.assertEqual(test_member.age, 28)

    def test_dob_not_greater_than_today(self):
        test_member = frappe.get_doc({
            "doctype": "Gym Member",
            "first_name": "Tony",
            "last_name": "Smith",
            "date_of_birth": str(dt.date.today() + dt.timedelta(days=1)),
            "email": "tony.smith@example.com",
            "phone": "9901234123"
        })

        with self.assertRaises(frappe.exceptions.ValidationError) as context:
            test_member.insert()

        self.assertTrue('Date of Birth cannot be greater than today' in str(context.exception))



