# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
# from gym_management.utils.helpers import get_end_time
import re


class GymClass(WebsiteGenerator):
    pass
    # def before_save(self):
    #     end_time = get_end_time(self.start_time, self.duration)
    #     route = re.sub(r'[^A-Za-z0-9-]', '-', self.name)
    #
    #     self.end_time = str(end_time)
    #     self.route = f"class/{route.lower()}"
