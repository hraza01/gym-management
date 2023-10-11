frappe.pages['gym-member-profile'].on_page_load = function(wrapper) {
	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Member Profile'),
		single_column: true
	});

	$(frappe.render_template("gym_member_profile")).appendTo(page.body.addClass("no-border"));
}
