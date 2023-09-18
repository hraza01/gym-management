import frappe
from frappe.query_builder.functions import Sum


def execute(filters=None):
    columns = [
        {
            "label": "Category",
            "options": "",
            "fieldname": "category",
            "fieldtype": "Data",
            "width": 230,
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Float",
            "precision": 2,
            "width": 230,
        },
    ]

    data = generate_data()

    chart_labels = [record['category'] for record in data]
    chart_data = [
        {
            "name": "Bookings by Class Type",
            "values": [record['revenue'] for record in data]
        },
    ]

    chart = generate_chart(chart_labels, chart_data)

    return columns, data, None, chart


def generate_data():
    memberships = frappe.qb.DocType("Gym Membership")
    trainer_subscriptions = frappe.qb.DocType("Gym Trainer Subscription")

    memberships_revenue = (frappe.qb
                           .from_(memberships)
                           .where(memberships.docstatus == 1)
                           .select(Sum(memberships.plan_fee).as_('revenue'))
                           ).run(as_dict=True)

    trainer_subscriptions_revenue = (frappe.qb
                                     .from_(trainer_subscriptions)
                                     .where(trainer_subscriptions.docstatus.isin([0, 1]))
                                     .select(Sum(trainer_subscriptions.trainer_fee).as_('revenue'))
                                     ).run(as_dict=True)

    memberships_revenue[0]['category'] = 'Gym Memberships'
    trainer_subscriptions_revenue[0]['category'] = 'Gym Trainer Subscriptions'

    return [*memberships_revenue, *trainer_subscriptions_revenue]


def generate_chart(labels, datasets):
    chart = {
        "type": "pie",
        "data": {
            "labels": labels,
            "datasets": datasets
        },
    }

    return chart
