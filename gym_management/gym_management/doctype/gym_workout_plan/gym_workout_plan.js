// Copyright (c) 2023, Hasan Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Workout Plan', {
  refresh(frm) {
  },

  member_id: function(frm) {
    console.log(frm.doc.member_id)

    frm.set_query("membership_no", () => {
      return {
        filters: {
          "gym_member": ["=", frm.doc.member_id],
        },
      };
    });
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
