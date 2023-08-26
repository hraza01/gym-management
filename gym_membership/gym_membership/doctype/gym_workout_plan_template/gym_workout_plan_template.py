# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
import re


class GymWorkoutPlanTemplate(WebsiteGenerator):
    def before_save(self):
        if not self.route:
            route = re.sub(r'[^A-Za-z0-9-]', '-', self.name)
            self.route = f"workout-plans/{route.lower()}"
