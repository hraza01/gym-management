# Copyright (c) 2023, Hasan Raza and contributors
# For license information, please see license.txt

import datetime as dt


def get_end_time(start_time, duration):
    return dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") + dt.timedelta(
        minutes=int(duration)
    )
