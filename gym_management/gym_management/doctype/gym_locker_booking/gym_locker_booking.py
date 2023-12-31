# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from gym_management.utils.helpers import get_end_time
import datetime as dt


class GymLockerBooking(Document):
    # pass
    def before_save(self):
        end_time = get_end_time(self.start_time, self.duration)
        self.end_time = str(end_time)


@frappe.whitelist()
def get_available_lockers(start_time, duration):
    gym_locker_bookings = frappe.qb.DocType("Gym Locker Booking")
    gym_lockers = frappe.qb.DocType("Gym Locker")

    start = dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = get_end_time(start_time, duration)

    # ALL BOOKED LOCKERS FOR THE SPECIFIED TIMEFRAME
    sub_query = (
        frappe.qb.from_(gym_locker_bookings)
        .select("locker")
        .distinct()
        .where(gym_locker_bookings.start_time >= start)
        .where(gym_locker_bookings.end_time <= end)
    ).run(as_dict=True)

    booked_lockers = [item.locker for item in sub_query]

    if not booked_lockers:
        return (frappe.qb.from_(gym_lockers).select("name").distinct()).run(
            as_dict=True
        )

    query = (
        frappe.qb.from_(gym_lockers)
        .select("name")
        .distinct()
        .where(gym_lockers.name.notin(booked_lockers))
    )

    return query.run(as_dict=True)
