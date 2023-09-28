frappe.ready(function() {
  frappe.web_form.on('member_id', (field, value) => {
    frappe.call({
      method: 'gym_management.gym_management.doctype.gym_membership.gym_membership.get_membership_detail',
      args: {
        member_id: value,
      }
    }).then(res => {
      try {
        const [{name: membership_no}] = res.message
        frappe.web_form.set_value('membership_no', membership_no)

      } catch (e) {
        frappe.web_form.set_value('membership_no', '')
        frappe.throw(`Unable to find an active membership for member ${value}`, "Membership Not Found")
      }
    })
  })
})
