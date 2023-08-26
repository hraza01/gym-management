// Copyright (c) 2023, Hasan Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Trainer Subscription", {
  refresh(frm) {
    frm.add_custom_button("Fetch Membership", () => {
      frappe.call({
        method: 'gym_membership.gym_membership.doctype.gym_membership.gym_membership.get_membership_detail',
        args: {
          member_id: frm.doc.member_id,
        }
      }).then(res => {
        let dialog = new frappe.ui.Dialog({
          title: "Fetch Membership",
          fields: [
            {
              fieldtype: "Select",
              fieldname: "membership_no",
              label: "Membership No",
              options: res.message.map(r => r.name)
            },
          ],
          primary_action_label: "Select",
          primary_action: (data) => {
            let { membership_no } = data
            frm.set_value('membership_no', membership_no)
            dialog.hide()
          }
        })

        dialog.show();
      })
    })
  },
});
