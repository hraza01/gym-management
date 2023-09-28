frappe.listview_settings['Gym Membership'] = {
	onload: function(listview) {

    const roles = ['System Manager', 'Gym Admin']
    const condition = roles.some((r) => frappe.user_roles.includes(r))

    if (!condition) {
      console.log(listview)
      frappe.route_options = {"email": ["=", frappe.session.user]};
		}
  }
};
