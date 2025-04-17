from django.db import models,transaction

# Create your models here.
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from DCB_Project.views import generate_unique_object_id
from UserManagement.models import *
from django.db.models import Index
import datetime
import pytz
import os
from django.conf import settings
import re
import uuid
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User
from django.utils import timezone

tz = pytz.timezone('Asia/Calcutta')
current_datetime = datetime.datetime.now(tz=tz)


ownership_type = (
    ('1st Owner', '1st Owner'),
    ('2nd Owner', '2nd Owner'),
    ('3rd Owner', '3rd Owner'),
    ('4rd Owner', '4rd Owner')
)

fuel_type = (
    ('CNG', 'CNG'),
    ('Hybrid', 'Hybrid'),
    ('Diesel', 'Diesel'),
    ('Petrol', 'Petrol'),
    ('Electric', 'Electric'),
    ('LPG', 'LPG'),

)

transmission_type = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual')
)

insurance_type = (
    ('Zero Dep', 'Zero Dep'),
    ('Comprehensive', 'Comprehensive'),
    ('Third Party', 'Third Party'),
    ('No Insurance', 'No Insurance')
)

air_conditional_type = (
    ('Automatic Climate Control', 'Automatic Climate Control'),
    ('Manual Control', 'Manual Control'),
    ('With Heater', 'With Heater'),
    ('Without Heater', 'Without Heater'),
    ('NO AC', 'NO AC'),
)

power_window_type = (
    ('Front Window Only', 'Front Window Only'),
    ('All Four Power Window', 'All Four Power Window')
)

adjustable_orvms_type = (
    ('Electrically Adjustable', 'Electrically Adjustable'),
    ('Manually Adjustable', 'Manually Adjustable')
)

lock_system_type = (
    ('Central Locking', 'Central Locking'),
    ('Remote Control Central Locking', 'Remote Control Central Locking')
)

vehicle_condition_type = (
    ('New', 'New'),
    ('Old', 'Old')
)

car_status = (
    ('Pending', 'Pending'),
    ('Approve', 'Approve'),
    ('Rejected', 'Rejected'),
    ('Processing', 'Processing')
)




class CarBrands(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(CarBrands, on_delete=models.DO_NOTHING, related_name='car_model')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarVariant(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name='car_model')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def car_image_upload_path(instance, filename):
    # Define a function to dynamically determine the upload path
    brand_name = instance.car_detail.variant.model.brand.name
    model_name = instance.car_detail.variant.model.name
    variant_name = instance.car_detail.variant.name
    if re.search(r'\s', brand_name):
        brand_name = brand_name.replace(' ', '_')
    if re.search(r'\s', model_name):
        model_name = model_name.replace(' ', '_')
    if re.search(r'\s', variant_name):
        variant_name = variant_name.replace(' ', '_')
    print('variant_name = ', variant_name, model_name)

    # if instance.variant.model.brand.name:
    #     brand_name =
    return f'car_images/{brand_name}/{model_name}/{variant_name}/{filename}'


#
# class CarColor(models.Model):
#     id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=False)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name

#
# class CarFuelType(models.Model):
#     id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=False)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name


# class InsuranceCompany(models.Model):
#     id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

class InsuranceCompany(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    founded_year = models.IntegerField()
    headquarters = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CarDetails(models.Model):
    YES_NO_CHOICES = [
            ('Yes', 'Yes'),
            ('No', 'No'),
        ]    
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    status = models.CharField(max_length=80, default='processing',null=True)
    previous_status = models.CharField(max_length=10, blank=True, null=True)
    # form_type = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('completed', 'Completed')], default='draft')
    is_draft = models.BooleanField(default=False)
    review = models.CharField(max_length=80, choices=car_status, default='processing')
    # Key Information
    variant = models.ForeignKey(CarVariant, on_delete=models.CASCADE, related_name='car_variant',null=True,blank=True)
    car_year = models.CharField(null=True,blank=True,max_length=50)
    ownership = models.CharField(max_length=50, choices=ownership_type,null=True,blank=True)
    color = models.CharField(max_length=50,null=True,blank=True)
    fuel_type = models.CharField(max_length=80, choices=fuel_type,null=True,blank=True)
    transmission = models.CharField(max_length=80,choices=transmission_type, null=True, blank=True)
    engine_capacity = models.CharField(max_length=80, null=True, blank=True)
    total_keys = models.CharField(max_length=50,null=True, blank=True)
    insurance_type = models.CharField(max_length=80, choices=insurance_type, null=True, blank=True)
    insurance_by = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, null=True,
                                     blank=True, related_name='car_insurance_by')
    insurance_validity = models.DateField(null=True, blank=True)
    fitness_validity = models.DateField(null=True, blank=True)
    pollution_validity = models.DateField(null=True, blank=True)
    registration_place = models.CharField(max_length=80, null=True, blank=True)
    registration_no = models.CharField(max_length=50, null=True, blank=True)
    total_km_driven = models.CharField(max_length=50,null=True, blank=True)
    demand_price = models.CharField(null=True,max_length=80)
    last_service_date = models.DateField(null=True, blank=True)
    vehicle_location = models.CharField(max_length=250, null=True, blank=True)
    # Interior
    power_steering = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    cruise_control = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    navigation_system = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    adjustable_steering = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    steering_control = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    air_conditioning = models.CharField(max_length=80,choices=power_window_type, null=True, blank=True)
    power_window = models.CharField(max_length=80,choices=power_window_type, null=True, blank=True)
    # Exteriors
    alloy_wheel = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    sun_roof = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    adjustable_orvm = models.CharField(max_length=80,choices=adjustable_orvms_type, null=True, blank=True)
    # Infotainment
    bluetooth = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    am_fm_radio = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    usb_compatibility = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='Yes',null=True,blank=True)
    aux_compatibility = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='Yes',null=True,blank=True)
    android_car_play = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    wireless_charger = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    # safety
    abs = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='Yes',null=True,blank=True)
    ebd = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='Yes',null=True,blank=True)
    anti_theft_device = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    rear_parking_camera = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    rear_parking_sensor = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    front_parking_camera = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    lock_system = models.CharField(max_length=80, choices=lock_system_type, null=True, blank=True)
    total_air_bag = models.CharField(max_length=50,null=True, blank=True)
    # vehicle condition
    battery_status = models.CharField(max_length=80, choices=vehicle_condition_type, null=True, blank=True)
    tyre_condition = models.CharField(max_length=80, choices=vehicle_condition_type, null=True, blank=True)
    vehicle_warranty = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    vehicle_warranty_date = models.DateField(null=True, blank=True)
    accidental = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    # Additional Services to be offered
    finance = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    exchange = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)
    extended_warranty = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No',null=True,blank=True)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.id
    
    def get_status(self):
        today = timezone.now().date()
        if self.fitness_validity or self.pollution_validity or self.insurance_validity:
            expiry_date = self.fitness_validity - relativedelta(days=1)
            if expiry_date < today:
                self.status = "expired"
                return "expired"
        else:
            return "live"    
        

class DraftCarDetails(CarDetails):
    # is_draft = models.BooleanField(default=True)
    draft_saved_at = models.DateTimeField(auto_now=True)  # Timestamp for when the draft was saved

    class Meta:
        verbose_name = 'Draft Car Detail'
        verbose_name_plural = 'Draft Car Details'

    def __str__(self):
        return self.id




class Lead(models.Model):
    STATUS_CHOICES = [
        ('cold', 'Cold'),
        ('warm', 'Warm'),
        ('hot', 'Hot'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null= True, blank= True)
    user_type = models.CharField(max_length=10, default='Customer')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='cold')
    visit_time = models.DateTimeField(default=timezone.now)
    page_stay_duration = models.IntegerField(default=0)  # Store duration in seconds
    visit_count = models.IntegerField(default=0)  
    made_enquiry = models.BooleanField(default=False)
    viewed_car = models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name='car_detail', null= True, blank= True)
    def __str__(self):
        return f"{self.user.phone} - {self.status}"


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null= True, blank= True)  # Link to user
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    car =  models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name='schedule_car', null= True, blank= True)
    source = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        unique_together = ('user', 'message')  # Ensure unique notifications per user/message/car combo
        ordering = ['-created_at']  # Order notifications by most recent
        
    def __str__(self):
        # Check if the car and its related fields are available before trying to access them
        if self.car and self.car.variant and self.car.variant.model and self.car.variant.model.brand:
            return f"Notification for {self.car.variant.model.brand.name} {self.car.variant.model.name} {self.car.variant.name} - {self.message}"
        else:
            # Provide a fallback message if any related field is missing
            return f"Notification - {self.message}"

class CarViews(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    car_id = models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name='car_view')
    view_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='view_by')
    total_view = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_id




class WishlistCar(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    car_id = models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name='wishlist_car')
    wishlist_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wishlist_by')
    is_wishlist = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_id
        

class CarImage(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    car_detail = models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name='car_image_detail')
    image = models.ImageField(upload_to=car_image_upload_path)
    is_thumbnail = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name





class Insurance(models.Model):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    phone_regex = RegexValidator(regex=r'^[6789]\d{9}$',
                                 message="Phone number must be 10 digit no and started from 6 to 9 ...")
    user_phone_no = models.CharField(max_length=15, validators=[phone_regex])
    # user_name = models.CharField(max_length=200)
    insured_name = models.CharField(max_length=200)
    # user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='insured_user')
    policy_no = models.CharField(max_length=80)
    insurer_name = models.CharField(max_length=300)
    # insurance_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=80, null=True, blank=True)
    product = models.CharField(max_length=80, null=True, blank=True)
    policy_type = models.CharField(max_length=80, null=True, blank=True)
    is_new_policy = models.BooleanField(default=False)
    is_renewal = models.BooleanField(default=False)
    risk_start_date = models.DateField(null=True, blank=True)
    risk_end_date = models.DateField(null=True, blank=True)
    ncb_status = models.CharField(max_length=80, null=True, blank=True)
    idv = models.CharField(null=True,max_length=80)
    total_premium = models.CharField(null=True,max_length=80)
    fuel_type = models.CharField(max_length=80, choices=fuel_type)
    car_model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name='insurance_car_model')
    rto_state = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    next_renewal_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)    

    def get_status(self):
        today = timezone.now().date()
        expiry_date = self.risk_start_date + relativedelta(months=12) - relativedelta(days=1)
        
        if expiry_date < today:
            return "expired"
        # Check if the warranty is within 30 days of expiry (renewal period)
        elif expiry_date - timedelta(days=30) <= today <= expiry_date:
            return "renew"
        # Otherwise, it's still live
        else:
            return "live"

    def __str__(self):
        return self.user_phone_no



class Warranty(models.Model):
    # id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    # order_id = models.CharField(max_length=80, unique=True)
    # order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # name_validator = RegexValidator(
    #     regex=r'^[A-Z][a-z]*$',  # Pattern to match valid names
    #     message="Name must start with a capital letter and contain only alphabetic characters."
    # )    
    phone_regex = RegexValidator(regex=r'^[6789]\d{9}$',
                                 message="Phone number must be 10 digit no and started from 6 to 9 ...")
    user_phone_no = models.CharField(max_length=15, validators=[phone_regex])
    user_name = models.CharField(max_length=200)
    # user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='warranty_user')
    vehicle_registration_no = models.CharField(max_length=50)
    warranty_period =models.PositiveIntegerField()
    purchase_date = models.DateField()
    roadside_assistant_date = models.DateField(null=True, blank=True)
    warranty_type = models.CharField(max_length=30,default='Comprehensive')

    next_renewal_date = models.DateField(null=True, blank=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name='warranty_car_model')
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=100, unique=True,blank=True,null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # self.full_clean()  # This will call clean() method and validate the model
        if not self.order_id:
            self.order_id = f"DCBW-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)    
    # def save(self, *args, **kwargs):
    #     if not self.order_id:
    #         self.order_id = f"DCBW-{uuid.uuid4().hex[:8].upper()}"
    #     super().save(*args, **kwargs)
 
    def __str__(self):
        return self.user_name

    def get_status(self):
        today = timezone.now().date()
        expiry_date = self.purchase_date + relativedelta(months=self.warranty_period) - relativedelta(days=1)
        
        if expiry_date < today:
            return "expired"
        # Check if the warranty is within 30 days of expiry (renewal period)
        elif expiry_date - timedelta(days=30) <= today <= expiry_date:
            return "renew"
        # Otherwise, it's still live
        else:
            return "live"
