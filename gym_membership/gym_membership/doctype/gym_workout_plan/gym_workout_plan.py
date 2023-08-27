# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymWorkoutPlan(Document):

    def before_save(self):
        self.total_duration, self.total_burn = get_totals(self.workouts)


def get_totals(workouts):
    total_duration = 0
    total_burn = 0

    for workout in workouts:
        total_duration += workout.duration_minutes
        total_burn += (workout.calorie_burn_rate / 60) * workout.duration_minutes

    return total_duration, total_burn
