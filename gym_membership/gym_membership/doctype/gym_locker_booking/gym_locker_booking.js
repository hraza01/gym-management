// Copyright (c) 2023, Hasan Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Locker Booking", {
	refresh(frm) {
    frm.add_custom_button("Find Available Lockers", () => {
      frappe.call({
        method: 'gym_membership.gym_membership.doctype.gym_locker_booking.gym_locker_booking.get_available_lockers',
        args: {
          start_time: frm.doc.start_time,
          duration: frm.doc.duration
        }
      }).then(res => {
        let dialog = new frappe.ui.Dialog({
          title: "Find a Locker",
          fields: [
            {
              fieldtype: "Select",
              fieldname: "locker",
              label: "Locker",
              options: res.message.map(r => r.name)
            },
          ],
          primary_action_label: "Select",
          primary_action: (data) => {
            let { locker } = data
            frm.set_value('locker', locker)
            dialog.hide()
          }
        })

        dialog.show();
      })
    })
	},
});
