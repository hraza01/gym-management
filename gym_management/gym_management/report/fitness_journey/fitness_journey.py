# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import Order


def execute(filters=None):
    columns = [
        {
            "label": "Start Date",
            "options": "",
            "fieldname": "start_date",
            "fieldtype": "Date",
            "width": 230,
        },
        {
            "label": "End Date",
            "options": "",
            "fieldname": "end_date",
            "fieldtype": "Date",
            "width": 230,
        },
        {
            "label": "Member",
            "options": "Gym Member",
            "fieldname": "member_id",
            "fieldtype": "Link",
            "width": 230,
        },
        {
            "label": "Member Name",
            "options": "",
            "fieldname": "member_name",
            "fieldtype": "Data",
            "width": 230,
        },
        {
            "label": "Weight",
            "options": "",
            "fieldname": "current_weight",
            "fieldtype": "Int",
            "width": 230,
        },
        {
            "label": "Daily Calorie Intake",
            "options": "",
            "fieldname": "calorie_intake_required",
            "fieldtype": "Int",
            "width": 230,
        },
        {
            "label": "Total Daily Duration (mins)",
            "options": "",
            "fieldname": "total_duration",
            "fieldtype": "Int",
            "width": 230,
        },
        {
            "label": "Total Daily Burn",
            "options": "",
            "fieldname": "total_burn",
            "fieldtype": "Int",
            "width": 230,
        }
    ]

    data = generate_data(filters.member_id)

    chart_labels = [str(record['start_date']) for record in data]
    chart_data = [
        {
            "name": "Calorie Intake",
            "chartType": "bar",
            "values": [record['calorie_intake_required'] for record in data]
        },
        {
            "name": "Weight",
            "chartType": "line",
            "values": [record['current_weight'] for record in data]
        },
        {
            "name": "Calorie Burn",
            "chartType": "line",
            "values": [record['total_burn'] for record in data]
        },
    ]

    chart = generate_chart(chart_labels, chart_data)

    return columns, data, None, chart


def generate_data(member_id):
    gym_workouts = frappe.qb.DocType("Gym Workout Plan")

    query = (frappe.qb
             .from_(gym_workouts)
             .where(gym_workouts.docstatus == 1)
             .where(gym_workouts.member_id == member_id)
             .orderby(gym_workouts.start_date, order=Order.asc)
             .select('name', 'member_id', 'member_name', 'start_date', 'end_date', 'current_weight',
                     'calorie_intake_required', 'total_duration', 'total_burn')
             )

    return query.run(as_dict=True)


def generate_chart(labels, datasets):
    chart = {
        "type": "axis-mixed",
        "data": {
            "labels": labels,
            "datasets": datasets
        },
    }

    return chart
