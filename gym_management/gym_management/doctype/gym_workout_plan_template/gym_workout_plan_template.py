# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from gym_management.gym_management.doctype.gym_workout_plan.gym_workout_plan import (
    get_totals,
)
import re


class GymWorkoutPlanTemplate(WebsiteGenerator):
    def before_save(self):
        self.total_duration, self.total_burn = get_totals(self.workouts)

        route = re.sub(r"[^A-Za-z0-9-]", "-", self.name)
        self.route = f"workout-plans/{route.lower()}"
