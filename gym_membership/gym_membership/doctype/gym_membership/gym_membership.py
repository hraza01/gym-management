# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.query_builder import Order, Criterion


class GymMembership(Document):

    def before_save(self):
        exists = frappe.db.exists(
            'Gym Membership',
            {
                'gym_member': self.gym_member,
                'docstatus': 1,
                'end_date': ('>', self.end_date),
            },
        )
        if exists:
            frappe.throw('There is an active membership for this member')


@frappe.whitelist()
def get_membership_detail(member_id):
    gym_memberships = frappe.qb.DocType("Gym Membership")

    query = (
        frappe.qb.from_(gym_memberships)
        .where(
            Criterion.all(
                [
                    gym_memberships.docstatus == 1,
                    gym_memberships.gym_member == member_id,
                ]
            )
        )
        .orderby(gym_memberships.end_date, order=Order.desc)
        .limit(1)
        .select("name")
    )

    if not query:
        frappe.throw(f"Unable to find membership for Member {member_id}")

    return query.run(as_dict=True)
