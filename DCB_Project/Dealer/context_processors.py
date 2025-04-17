# context_processors.py
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from ProductManagement.models import *

def expired_warranty(request):
    today = timezone.now().date()
    user = request.user
    # Fetch all warranties and compute their expiry dates
    warranties = Warranty.objects.filter(created_by=user)
    current_warranties = []
    expired_warranties = []

    for warranty in warranties:
        expiry_date = warranty.purchase_date + relativedelta(months=warranty.warranty_period) -relativedelta(days=1)
        reminder_date = expiry_date - timedelta(days=5)
        # Append warranty object to the appropriate list
        if expiry_date >= today:
            if warranty.get_status() == 'renew':
                current_warranties.append((warranty,expiry_date,reminder_date))
        else:
            expired_warranties.append((warranty,expiry_date,reminder_date))
    
    expired_warranties.sort(key=lambda x: x[1])
    
    # Render the template with the sorted warranties
    return expired_warranties, current_warranties



def other_notification(request):
    expired,live = expired_warranty(request)
    notifications = []
    today = timezone.now().date()
    for warranty in live:
        expiry = warranty[1]
        reminder = warranty[2]
        brand = warranty[0].car_model.brand.name
        model = warranty[0].car_model.name
        phone = warranty[0].user_phone_no
        diff = (expiry - today).days
        name = warranty[0].created_by.get_full_name()
        if today < expiry:
            msg = f"User {name} with contact {phone} warranty is about to expire in {diff} days. Kindly renew on the Warranty page."
            try:
                notification, created = Notification.objects.get_or_create(
                    user=request.user,
                    message=msg
                )
                if created:  # Only add if it was newly created
                    notifications.append(notification)
            except IntegrityError:
                # If a duplicate notification was attempted, skip it
                continue

    return notifications

#insurances notifications
def active_insurances(request):
    today = timezone.now().date()

    insurances = Insurance.objects.filter(created_by= request.user)
    current = []

    for insurance in insurances:
        if insurance.risk_start_date is None:
            continue
        expiry_date = insurance.risk_start_date + relativedelta(months=12) -relativedelta(days=1)
        reminder_date = expiry_date - timedelta(days=5)
        # Append insurance object to the appropriate list
        if expiry_date >= today:
            if insurance.get_status() == 'renew':
                current.append((insurance,expiry_date,reminder_date))
        
    return current

def notify_insurance(request):
    live = active_insurances(request)
    notify = []
    today = timezone.now().date()
    for insurance in live:
        expiry = insurance[1]
        name = insurance[0].created_by.get_full_name()
        phone = insurance[0].user_phone_no
        diff = (expiry - today).days
        if today < expiry:
            msg = f"User {name} with contact {phone} Insurance is about to expire in {diff} days. Kindly renew on the Insurance page."
            try:
                notification, created = Notification.objects.get_or_create(user=request.user, message=msg)
                if created:
                    notify.append(notification)
            except IntegrityError:
                continue
            
    return notify

def notification_processor(request):
    notifications = []

    if request.user.is_authenticated:
        three_days_ago = timezone.now() - timedelta(days=3)
        temp_notifications = Notification.objects.filter(
            user=request.user,
            created_at__gte=three_days_ago
        ).order_by('-created_at')
        
        # Extend notifications with unique entries
        notifications.extend(temp_notifications)

        # Fetch and add unique notifications from `other_notification`
        other_notifs = other_notification(request)
        notifications.extend(other_notifs)
        approvals = Notification.objects.filter(user=request.user, source='admin')
        # if admin:
        #     notifications.extend(list(admin))
        for each in approvals:
            if each not in notifications:
                notifications.append(each)
        
        insurance_notification = notify_insurance(request)
        notifications.extend(insurance_notification)
        

    return {
        'notifications': notifications,
        'count': len(notifications),
    }





# def notification_processor(request):
#     notifications = []
#     if request.user.is_authenticated:
#         three_days_ago = timezone.now() - timedelta(days=3)
        
#         # Only fetch notifications within the last 3 days
#         lead_notifications = Notification.objects.filter(
#             car__created_by=request.user,
#             created_at__gte=three_days_ago
#         ).order_by('-created_at')
        
#         notifications.extend(list(lead_notifications))

#         # Get additional notifications from `other_notification`
#         others = other_notification(request)
#         for notif in others:
#             if notif not in notifications:
#                 notifications.append(notif)
        
#         count = len(notifications)
#     else:
#         count = 0

#     return {
#         'notifications': notifications,
#         'count': count,
#     }