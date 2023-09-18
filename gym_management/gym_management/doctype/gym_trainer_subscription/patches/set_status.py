import frappe
import datetime as dt


def execute():
    # set all trainer subs "status" to "completed" if docstatus != 2 AND end_date <= today
    trainer_subscriptions = frappe.get_all(
        "Gym Trainer Subscription",
        fields=["name", "docstatus", "status", "start_date", "end_date"],
        filters={
            "docstatus": ['in', [0, 1]]
        }
    )

    for doc in trainer_subscriptions:
        if doc.docstatus == 1 and doc.end_date <= dt.date.today() and doc.status == "In Progress":
            frappe.db.set_value("Gym Trainer Subscription", doc.name, "status", "Completed", update_modified=False)

