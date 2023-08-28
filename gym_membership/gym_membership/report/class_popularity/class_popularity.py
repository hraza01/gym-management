import frappe
from frappe.query_builder import Order
from frappe.query_builder.functions import Count


def execute(filters=None):
    columns = [
        {
            "label": "Class Type",
            "options": "",
            "fieldname": "class_type",
            "fieldtype": "Data",
            "width": 230,
        },
        {
            "label": "Bookings",
            "options": "",
            "fieldname": "bookings",
            "fieldtype": "Data",
            "width": 230,
        }
    ]

    data = generate_data()

    chart_labels = [record['class_type'] for record in data]
    chart_data = [
        {
            "name": "Bookings by Class Type",
            "values": [record['bookings'] for record in data]
        },
    ]

    chart = generate_chart(chart_labels, chart_data)

    return columns, data, None, chart


def generate_data():
    gym_class_registrations = frappe.qb.DocType("Gym Class Registration")

    query = (frappe.qb
             .from_(gym_class_registrations)
             .where(gym_class_registrations.docstatus.isin([0, 1]))
             .groupby(gym_class_registrations.class_type)
             .orderby('bookings', order=Order.desc)
             .select(gym_class_registrations.class_type,
                     Count(gym_class_registrations.name).distinct().as_('bookings'))
             )

    return query.run(as_dict=True)


def generate_chart(labels, datasets):
    chart = {
        "type": "pie",
        "data": {
            "labels": labels,
            "datasets": datasets
        },
    }

    return chart
