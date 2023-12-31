import frappe
import datetime as dt


def get_context(context):

    member_id = get_member_id(frappe.session.user)

    if member_id:

        context.member = member_id

        config = {
            'membership': {
                'fields': ['name', 'gym_plan', 'plan_fee', 'start_date', 'end_date'],
                'filters': {'gym_member': context.member, 'docstatus': 1}
            },
            'trainer_subscription': {
                'fields': ['name', 'gym_trainer', 'trainer_fee', 'start_date', 'end_date', 'status'],
                'filters': {'member_id': context.member, 'docstatus': ("!=", 2)}
            }
        }

        context.member_detail = frappe.get_doc('Gym Member', context.member)
        context.memberships = frappe.db.get_list('Gym Membership', fields=config['membership']['fields'],
                                                 filters=config['membership']['filters'], order_by='end_date desc')
        context.trainer_subscriptions = frappe.db.get_list('Gym Trainer Subscription',
                                                           fields=config['trainer_subscription']['fields'],
                                                           filters=config['trainer_subscription']['filters'],
                                                           order_by='end_date desc')

        context.membership_remaining_days = get_remaining_days(context.memberships[0].end_date)
        context.training_remaining_days = get_remaining_days(
            context.trainer_subscriptions[0].end_date) if context.trainer_subscriptions else 0

        return context


def get_remaining_days(end_date):
    today = dt.date.today()

    if today >= end_date:
        return 0

    return str((end_date - today).days)


def get_member_id(user_email):
    member_id = frappe.get_list("Gym Member", fields=["name"], filters={"email": user_email})

    if not member_id:
        return None

    return member_id[0]['name']
