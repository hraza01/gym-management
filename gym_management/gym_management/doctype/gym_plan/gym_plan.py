# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymPlan(Document):
    pass

    # def validate(self):
    #     """ Validates a training plan can only be selected once per trainer """
    #
    #     trainer_subscription = self.trainer_subscription
    #     unique_trainer_subscription = []
    #
    #     for idx, item in enumerate(trainer_subscription):
    #
    #         if item.gym_trainer in unique_trainer_subscription:
    #             trainer_subscription.pop(idx)
    #
    #         unique_trainer_subscription.append(item.gym_trainer)
    #
    # def get_total_amount(self) -> int:
    #     """ Returns the total ticket amount """
    #
    #     fee = self.plan_fee
    #
    #     for item in self.trainer_subscription:
    #         fee += item.trainer_fee
    #
    #     return fee
    #
    # def before_save(self):
    #     self.total_amount = self.get_total_amount()
