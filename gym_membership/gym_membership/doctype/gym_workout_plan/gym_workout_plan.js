// Copyright (c) 2023, Hasan Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Workout Plan', {
  refresh(frm) {
    frm.add_custom_button(
      'Fetch Membership',
      () => {
      frappe.call({
        method: 'gym_membership.gym_membership.utils.helpers.get_membership_detail',
        args: {
          member_id: frm.doc.member_id,
        }
      }).then(res => {
        let dialog = new frappe.ui.Dialog({
          title: 'Fetch Membership',
          fields: [
            {
              fieldtype: 'Select',
              fieldname: 'membership_no',
              label: 'Membership No',
              options: res.message.map(r => r.name)
            },
          ],
          primary_action_label: 'Select',
          primary_action: (data) => {
            let {membership_no} = data
            frm.set_value('membership_no', membership_no)
            dialog.hide()
          }
        })

        dialog.show()
      })
    })
  },
  workout_plan_template(frm) {
    frappe.db.get_doc(
      'Gym Workout Plan Template',
      frm.doc.workout_plan_template
    ).then(doc => {
      frm.set_value('workouts', doc.workouts)
    })
  }
})
