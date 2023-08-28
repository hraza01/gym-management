// Copyright (c) 2023, Hasan Raza and contributors
// For license information, please see license.txt

frappe.query_reports["Fitness Journey"] = {
	"filters": [
    {
      "fieldname":"member_id",
      "label": __("Gym Member"),
      "fieldtype": "Link",
      "options": "Gym Member",
      "reqd": 1
    },
	]
};
