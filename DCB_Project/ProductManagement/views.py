from django.shortcuts import render, HttpResponseRedirect
from .models import *
from ProductManagement.models import *
from UserManagement.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
import csv
from UserManagement.forms import *
from django.db.models import Exists, F, Subquery, OuterRef, Q
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.


# def Boolean_Choices(field_name):
#     result = False
#     if field_name == 'Yes':
#         result = True
#     return result

def Boolean_Choices(field_name):
    result = 'No'
    if field_name == 'Yes':
        result = 'Yes'
    return result

def str_to_int(field_name):
    try:
        return int(field_name)
    except:
        return field_name


def convert_empty_to_none(d):
    for key, value in d.items():
        if value == "":
            d[key] = None
    return d


def get_car_model(request):
    print('fkdsfsdv = ')
    car_brand_id = request.GET.get('car_brand_id')
    print('car_brand_id = ',car_brand_id)
    car_models = CarModel.objects.filter(is_active=True, brand=car_brand_id)
    car_model_data = [{'id': car_model.id, 'name': car_model.name.encode('ascii', 'ignore').decode('ascii')} for car_model in car_models]
    print('car_model_data = ', car_model_data)
    return JsonResponse(car_model_data, safe=False)


def get_car_variant(request):
    car_model = request.GET.get('car_model_id')
    car_variants = CarVariant.objects.filter(is_active=True, model=car_model)
    car_variant_data = [{'id': car_variant.id, 'name': car_variant.name} for car_variant in car_variants]
    return JsonResponse(car_variant_data, safe=False)
    


def wishlist_car(request, car_id):
    if request.user.is_authenticated:
        user = request.user
        wishlist_car_instance = WishlistCar.objects.filter(wishlist_by=user, car_id__id=car_id, is_active=True, is_wishlist=True)
        if not wishlist_car_instance.exists():
            car_detail_instance = CarDetails.objects.get(id=car_id)
            wishlist_car = WishlistCar(wishlist_by=user, car_id=car_detail_instance, is_active=True, is_wishlist=True)
            wishlist_car.save()
            messages.info(request, "Added to Withlist Car")
        else:
            messages.info(request, "Already Withlist")
        referrer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referrer)
    else:
        messages.warning(request, "Please SignUp/Login")
        referrer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referrer)
        

def view_car(request):
    if request.user.is_authenticated:
        user = request.user
        car_id = request.POST.get('car_id')
        car_view_instance = CarViews.objects.filter(view_by=user, car_id=car_id, is_active=True)
        if car_view_instance.exists():
            total_view = car_view_instance.last.total_view
            car_view_instance.update(total_view=total_view)
        else:
            car_view = CarViews(view_by=user, car_id=car_id, is_active=True, total_view=1)
            car_view.save()
        return "save"
    else:
        return HttpResponseRedirect('/')


def website_car_filter(request):
    user = request.user
    brand_id = request.GET.get('car_brand')
    model_id = request.GET.get('car_model')
    variant_id = request.GET.get('car_variants')
    # print('brand_id = ', brand_id)
    # print('model_id = ', model_id)
    # print('variant_id = ', variant_id)
    if variant_id:
        car_details_instance = CarDetails.objects.filter(variant=variant_id, is_active=True)
    elif model_id:
        car_details_instance = CarDetails.objects.filter(variant__model=model_id, is_active=True)
    elif brand_id:
        car_details_instance = CarDetails.objects.filter(variant__model__brand=brand_id, is_active=True)
    else:
        car_details_instance = None
    if brand_id and car_details_instance.exists():
        # print('car_details_instance = ', car_details_instance)
        # messages.info(request, str(car_details_instance.count()))
        form = LoginForm()
        car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
        all_car_details = car_details_instance.filter(is_active=True).annotate(car_image=Subquery(car_image)).order_by('-created_at')
        car_brand = CarBrands.objects.filter(is_active=True)
        # print('car_brand = ', car_brand)
        car_model = CarModel.objects.filter(is_active=True)
        car_variant = CarVariant.objects.filter(is_active=True)
        # total_car =
        # print('all_car_details = ', all_car_details)
        return render(request, "Website/product_details/product_detail.html",
                      {'form': form, 'all_car_details': all_car_details, 'car_brands': car_brand,
                       'car_models': car_model,
                       'car_variants': car_variant})

        # return HttpResponseRedirect(referrer)
        # return "save"
    else:
        # if car_details_instance.exists() == False:
            if brand_id:
                form = LoginForm()
                car_details_instance = CarDetails.objects.filter(variant__model__brand=brand_id, is_active=True)
                car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
                all_car_details = car_details_instance.filter(is_active=True).annotate(car_image=Subquery(car_image)).order_by('-created_at')
                return render(request, "Website/product_details/product_detail.html",
                            {'form': form, 'all_car_details': all_car_details})   
            else:
                messages.warning(request, "NO Car Found")
                referrer = request.META.get('HTTP_REFERER')
                return HttpResponseRedirect(referrer)
        

  

  
    
def save_draft(request):
    if request.user.is_authenticated:
        user = request.user
        phone_no = user.phone
        group_list = user.groups.values_list('name', flat=True)
        if request.method == 'POST':
            # Update car details and change status to completed
            save_as_draft = request.POST.get('save_as_draft')
            files = request.FILES.getlist('car_images')
            d = {}
            if save_as_draft:
                car = DraftCarDetails()
                car_variants = request.POST.get('car_variants')
                a = CarVariant.objects.get(id=car_variants)
                # d[a] = car_variants
            else:
                car_id = request.POST.get('draft_id')
                car = DraftCarDetails.objects.get(id=car_id)
                a = car.variant
            
            if a:
                car.variant = a
            else:
                messages.info(request,'Please Fill the required details!')
            
            car.car_brand = request.POST.get('car_brand')
            car.car_model = request.POST.get('car_model')  
            car.car_year = request.POST.get('car_year')
            car.ownership = request.POST.get('ownership')
            car.total_km_driven = request.POST.get('total_km')
            car.color = request.POST.get('car_color')
            car.fuel_type = request.POST.get('fuel_type')
            car.transmission = request.POST.get('car_transmission')
            car.total_keys = request.POST.get('total_keys')
            car.engine_capacity = request.POST.get('engine_capacity')
            car.insurance_type = request.POST.get('insurance_type')
            car.insurance_validity = request.POST.get('insurance_validity')
            car.fitness_validity = request.POST.get('fitness_validity')
            car.pollution_validity = request.POST.get('pollution_validity')
            car.registration_place = request.POST.get('registration_place')
            car.registration_no = request.POST.get('registration_no')
            car.demand_price = request.POST.get('demand_price')
            car.last_service_date = request.POST.get('last_service')
            car.vehicle_location = request.POST.get('vehicle_location')
            car.power_steering = request.POST.get('power_steering')
            car.cruise_control = request.POST.get('cruise_control')
            car.navigation_system = request.POST.get('navigation_system')
            car.adjustable_steering = request.POST.get('adjustable_steering')
            car.adjustable_orvm = request.POST.get('adjustable_orvm')
            car.steering_control = request.POST.get('steering_control')
            car.air_conditioning = request.POST.get('air_conditioning')
            car.power_window = request.POST.get('power_window')
            car.alloy_wheel = request.POST.get('alloy_wheel')
            car.sun_roof = request.POST.get('sun_roof')
            car.bluetooth = request.POST.get('bluetooth')
            car.aux_compatibility = request.POST.get('aux_compatibility')
            car.adjustable_orvm  = request.POST.get('adjustable_orvm')
            car.am_fm_radio = request.POST.get('am_radio')
            car.android_car_play = request.POST.get('android_car_play')
            car.usb_compatibility = request.POST.get('usb_compatibility')
            car.wireless_charger = request.POST.get('wireless_charger')
            car.abs = request.POST.get('abs')
            car.rear_parking_sensor = request.POST.get('rear_parking_sensor')
            car.ebd = request.POST.get('ebd')
            car.lock_system = request.POST.get('lock_sensor')
            car.anti_theft_device = request.POST.get('anti_theft_device')
            car.total_air_bag = request.POST.get('total_air_bag')
            car.rear_parking_camera = request.POST.get('rear_parking_camera')
            car.battery_status = request.POST.get('battery_status')
            car.vehicle_warranty = request.POST.get('vehicle_certificate')
            car.vehicle_warranty_date = request.POST.get('vehicle_certificate_validity')
            car.tyre_condition = request.POST.get('tyre_condition')
            car.accidental = request.POST.get('accidental')
            car.finance = request.POST.get('finance')
            car.extended_warranty = request.POST.get('extended_warranty')
            car.exchange = request.POST.get('exchange')
            car.description = request.POST.get('description')
            # car.form_type = 'completed'
            car.is_draft = True
            # car.created_by = user 
            if car.insurance_type == "No Insurance":
                car.insurance_validity = None
            if car.fitness_validity == "":
                car.fitness_validity = None
            if car.pollution_validity == "":
                car.pollution_validity = None
            if car.last_service_date == "":
                car.last_service_date = None
            if car.insurance_validity == "":
                car.insurance_validity = None
                
                
            car.save()
            messages.success(request, 'Car details updated successfully!')
            referrer = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(referrer,{'car_detail':car})

    return HttpResponse(status=405)  # Method not allowed if not POST
    
def make_live(request,draft_id):
    if request.method == 'POST':
        # car = get_object_or_404(DraftCarDetails, id=id)
        
        car = DraftCarDetails.objects.get(id=draft_id) 
        # Update the car status to 'live' or appropriate status
        if car.is_draft:
            car.status = "live"
            car.previous_status = None
            car.is_draft = False
            car.save()
            messages.info(request, "Made Live Successfully !!")
            return HttpResponseRedirect('/dealer/car_list/')
            
    return HttpResponse(status=405)

def resume_form(request, car_id):
    car = get_object_or_404(CarDetails, id=car_id)
    car_images = CarImage.objects.filter(car_detail= car)
    yes_no_options = [('Yes', 'Yes'), ('No', 'No')]
    user = request.user
    # all_car_details = CarDetails.objects.filter(created_by=user)
    car_brand = CarBrands.objects.filter(is_active=True)
    car_model = CarModel.objects.filter(is_active=True)
    car_variant = CarVariant.objects.filter(is_active=True)
        
    context = {
        'car_detail': car,
        'car_images':car_images,
        'car_brands': car_brand,
        'car_models': car_model,
        'car_variants': car_variant,
        'yes_no_options': yes_no_options,
    }
        
    return render(request, 'Dealer/product/view-modal.html', context)



def save_car(request):
    if request.user.is_authenticated:
        user = request.user
        phone_no = user.phone
        # print('user =  = ', user)
        # print('phone = ', user.phone)
        # login_user = CustomUser.objects.get(username=login_user)
        # user_instance = CustomUser.objects.get(phone=phone_no)
        group_list = user.groups.values_list('name', flat=True)
        if request.method == 'POST':
            
            files = request.FILES.getlist('car_images')
            # print('images = ', files)
            # for file in files:
                # Image.objects.create(title=title, images=file)
                # print('car_image = ', file)
            car_brand = request.POST.get('car_brand')
            car_model = request.POST.get('car_model')
            car_variants = request.POST.get('car_variants')
            car_year = request.POST.get('car_year')
            ownership = request.POST.get('ownership')
            total_km_driven = request.POST.get('total_km')
            car_color = request.POST.get('car_color')
            fuel_type = request.POST.get('fuel_type')
            car_transmission = request.POST.get('car_transmission')
            total_keys = request.POST.get('total_keys')
            engine_capacity = request.POST.get('engine_capacity')
            insurance_type = request.POST.get('insurance_type')
            insurance_validity = request.POST.get('insurance_validity')
            fitness_validity = request.POST.get('fitness_validity')
            pollution_validity = request.POST.get('pollution_validity')
            last_service = request.POST.get('last_service')
            vehicle_location = request.POST.get('vehicle_location')
            registration_place = request.POST.get('registration_place')
            registration_no = request.POST.get('registration_no')
            demand_price = request.POST.get('demand_price')
            power_steering = request.POST.get('power_steering')
            cruise_control = request.POST.get('cruise_control')
            navigation_system = request.POST.get('navigation_system')
            adjustable_steering = request.POST.get('adjustable_steering')
            adjustable_orvm = request.POST.get('adjustable_orvm')
            steering_control = request.POST.get('steering_control')
            air_conditioning = request.POST.get('air_conditioning')
            power_window = request.POST.get('power_window')
            alloy_wheel = request.POST.get('alloy_wheel')
            sun_roof = request.POST.get('sun_roof')
            bluetooth = request.POST.get('bluetooth')
            aux_compatibility = request.POST.get('aux_compatibility')
            am_radio = request.POST.get('am_radio')
            android_car_play = request.POST.get('android_car_play')
            usb_compatibility = request.POST.get('usb_compatibility')
            wireless_charger = request.POST.get('wireless_charger')
            abs = request.POST.get('abs')
            rear_parking_sensor = request.POST.get('rear_parking_sensor')
            ebd = request.POST.get('ebd')
            lock_sensor = request.POST.get('lock_sensor')
            anti_theft_device = request.POST.get('anti_theft_device')
            total_air_bag = request.POST.get('total_air_bag')
            rear_parking_camera = request.POST.get('rear_parking_camera')
            battery_status = request.POST.get('battery_status')
            vehicle_certificate = request.POST.get('vehicle_certificate')
            vehicle_certificate_validity = request.POST.get('vehicle_certificate_validity')
            tyre_condition = request.POST.get('tyre_condition')
            accidental = request.POST.get('accidental')
            finance = request.POST.get('finance')
            extended_warranty = request.POST.get('extended_warranty')
            exchange = request.POST.get('exchange')
            description = request.POST.get('description')

            car_year = str_to_int(car_year)
            total_keys = str_to_int(total_keys)
            total_km_driven = str_to_int(total_km_driven)
            demand_price = str_to_int(demand_price)
            total_air_bag = str_to_int(total_air_bag)

            power_steering = Boolean_Choices(power_steering)
            cruise_control = Boolean_Choices(cruise_control)
            navigation_system = Boolean_Choices(navigation_system)
            adjustable_steering = Boolean_Choices(adjustable_steering)
            adjustable_orvm = Boolean_Choices(adjustable_orvm)
            steering_control = Boolean_Choices(steering_control)
            # air_conditioning = Boolean_Choices(air_conditioning)
            alloy_wheel = Boolean_Choices(alloy_wheel)
            sun_roof = Boolean_Choices(sun_roof)
            bluetooth = Boolean_Choices(bluetooth)
            aux_compatibility = Boolean_Choices(aux_compatibility)
            am_radio = Boolean_Choices(am_radio)
            android_car_play = Boolean_Choices(android_car_play)
            usb_compatibility = Boolean_Choices(usb_compatibility)
            wireless_charger = Boolean_Choices(wireless_charger)
            abs = Boolean_Choices(abs)
            ebd = Boolean_Choices(ebd)
            anti_theft_device = Boolean_Choices(anti_theft_device)
            rear_parking_camera = Boolean_Choices(rear_parking_camera)
            lock_sensor = Boolean_Choices(lock_sensor)
            vehicle_certificate = Boolean_Choices(vehicle_certificate)
            accidental = Boolean_Choices(accidental)
            finance = Boolean_Choices(finance)
            extended_warranty = Boolean_Choices(extended_warranty)
            rear_parking_sensor = Boolean_Choices(rear_parking_sensor)
            exchange = Boolean_Choices(exchange)
            try:
                a = CarVariant.objects.get(id=car_variants)
                
            except:
                error_message = ""
                if 'Dealer' in group_list:
                    messages.warning(request, "Please Fill tha Car Details")
                    return HttpResponseRedirect('/dealer/add_car/')
                else:
                    messages.warning(request, "Please Fill tha Car Details")
                    return HttpResponseRedirect('/add_car/')

            data = {'variant': a, 'car_year': car_year,
                    'ownership': ownership, 'total_km_driven': total_km_driven, 'color': car_color, 'fuel_type': fuel_type,
                    'transmission': car_transmission, 'total_keys': total_keys, 'engine_capacity': engine_capacity,
                    'insurance_type': insurance_type, 'insurance_validity': insurance_validity,
                    'fitness_validity': fitness_validity, 'pollution_validity': pollution_validity, 'last_service_date':last_service,
                    'registration_place': registration_place, 'registration_no': registration_no,'vehicle_location':vehicle_location,
                    'demand_price': demand_price, 'power_steering': power_steering, 'cruise_control': cruise_control,
                    'navigation_system': navigation_system, 'adjustable_steering': adjustable_steering,
                    'adjustable_orvm': adjustable_orvm, 'steering_control': steering_control,
                    'air_conditioning': air_conditioning,
                    'power_window': power_window, 'alloy_wheel': alloy_wheel, 'sun_roof': sun_roof,
                    'bluetooth': bluetooth,
                    'aux_compatibility': aux_compatibility, 'am_fm_radio': am_radio, 'android_car_play': android_car_play,
                    'usb_compatibility': usb_compatibility, 'wireless_charger': wireless_charger, 'abs': abs,
                    'rear_parking_sensor': rear_parking_sensor, 'ebd': ebd, 'lock_system': lock_sensor,
                    'anti_theft_device': anti_theft_device, 'total_air_bag': total_air_bag,
                    'rear_parking_camera': rear_parking_camera,
                    'battery_status': battery_status, 'vehicle_warranty': vehicle_certificate,
                    'vehicle_warranty_date': vehicle_certificate_validity, 'tyre_condition': tyre_condition,
                    'accidental': accidental, 'finance': finance, 'extended_warranty': extended_warranty,
                    'exchange': exchange, 'description': description, 'created_by': user, 'is_active': True}
            # data = {'variant': a, 'car_year': car_year,
            #         'ownership': ownership, 'total_km_driven': total_km_driven}
            data = convert_empty_to_none(data)
            # print('data = ', data)
            try: 
                total_car_add = CarDetails.objects.filter(created_by=user).count()
                # print('total_car_add = ', total_car_add)
                if 'Customer' in group_list and 'Dealer'not in group_list and total_car_add > 2:
                    messages.info(request, "Already add 2 car !!")
                    referrer = request.META.get('HTTP_REFERER')
                    return HttpResponseRedirect(referrer) 
                
                # elif 'save_draft' in request.POST:
                #     car = CarDetails.objects.create(**data, form_type='draft')
                #     return redirect('processing_tab')
                
                
                else:
                    print('dskfndsnf')
                    car_details_instance = CarDetails(**data)
                    print('car_details_instance = ', car_details_instance)
                    car_details_instance.save()
                    car_detail = CarDetails.objects.order_by('created_at').last()
                    print('car_detail 11233 = ', car_detail)
                    for file in files:
                        CarImage.objects.create(car_detail=car_detail, image=file, name=file.name, is_active=True, created_by=user)
                        print('car_image = ', file)
            except ValidationError as e:
                print('ndsndfsn')
                # Handle validation errors
                error_message = "Validation error: " + ", ".join(e.messages)
                print('error_message = ', error_message)
            messages.info(request, "Car Add Successfully")
            if 'Dealer' in group_list:
                return HttpResponseRedirect('/dealer/car_list/')
            else:
                return HttpResponseRedirect('/profile/')
        else:
            return render(request, "Customer/profile/profile.html")
    else:
        return HttpResponseRedirect('/')


def edit_car(request, car_id):
    if request.user.is_authenticated:
        car_detail = CarDetails.objects.filter(id=car_id).last()
        car_brand = CarBrands.objects.filter(is_active=True)
        # print('car_brand = ', car_brand)
        car_model = CarModel.objects.filter(is_active=True)
        car_variant = CarVariant.objects.filter(is_active=True)
        # car_detail = CarDetails.objects.get(id=car_id)
        if request.method == 'POST':
            files = request.FILES.getlist('car_images')
            print('images = ', files)
            # for file in files:
                # Image.objects.create(title=title, images=file)
                # print('car_image = ', file)
            car_brand = request.POST.get('car_brand')
            car_model = request.POST.get('car_model')
            car_variants = request.POST.get('car_variants')
            car_year = request.POST.get('car_year')
            ownership = request.POST.get('ownership')
            total_km_driven = request.POST.get('total_km')
            car_color = request.POST.get('car_color')
            fuel_type = request.POST.get('fuel_type')
            car_transmission = request.POST.get('car_transmission')
            total_keys = request.POST.get('total_keys')
            engine_capacity = request.POST.get('engine_capacity')
            insurance_type = request.POST.get('insurance_type')
            insurance_validity = request.POST.get('insurance_validity')
            fitness_validity = request.POST.get('fitness_validity')
            pollution_validity = request.POST.get('pollution_validity')
            registration_place = request.POST.get('registration_place')
            registration_no = request.POST.get('registration_no')
            demand_price = request.POST.get('demand_price')
            power_steering = request.POST.get('power_steering')
            cruise_control = request.POST.get('cruise_control')
            navigation_system = request.POST.get('navigation_system')
            adjustable_steering = request.POST.get('adjustable_steering')
            adjustable_orvm = request.POST.get('adjustable_orvm')
            steering_control = request.POST.get('steering_control')
            air_conditioning = request.POST.get('air_conditioning')
            power_window = request.POST.get('power_window')
            alloy_wheel = request.POST.get('alloy_wheel')
            sun_roof = request.POST.get('sun_roof')
            bluetooth = request.POST.get('bluetooth')
            aux_compatibility = request.POST.get('aux_compatibility')
            am_radio = request.POST.get('am_radio')
            android_car_play = request.POST.get('android_car_play')
            usb_compatibility = request.POST.get('usb_compatibility')
            wireless_charger = request.POST.get('wireless_charger')
            abs = request.POST.get('abs')
            rear_parking_sensor = request.POST.get('rear_parking_sensor')
            ebd = request.POST.get('ebd')
            lock_sensor = request.POST.get('lock_sensor')
            anti_theft_device = request.POST.get('anti_theft_device')
            total_air_bag = request.POST.get('total_air_bag')
            rear_parking_camera = request.POST.get('rear_parking_camera')
            battery_status = request.POST.get('battery_status')
            vehicle_certificate = request.POST.get('vehicle_certificate')
            vehicle_certificate_validity = request.POST.get('vehicle_certificate_validity')
            tyre_condition = request.POST.get('tyre_condition')
            accidental = request.POST.get('accidental')
            finance = request.POST.get('finance')
            extended_warranty = request.POST.get('extended_warranty')
            exchange = request.POST.get('exchange')
            description = request.POST.get('description')

            car_year = str_to_int(car_year)
            total_keys = str_to_int(total_keys)
            total_km_driven = str_to_int(total_km_driven)
            demand_price = str_to_int(demand_price)
            total_air_bag = str_to_int(total_air_bag)

            power_steering = Boolean_Choices(power_steering)
            cruise_control = Boolean_Choices(cruise_control)
            navigation_system = Boolean_Choices(navigation_system)
            adjustable_steering = Boolean_Choices(adjustable_steering)
            adjustable_orvm = Boolean_Choices(adjustable_orvm)
            steering_control = Boolean_Choices(steering_control)
            air_conditioning = Boolean_Choices(air_conditioning)
            alloy_wheel = Boolean_Choices(alloy_wheel)
            sun_roof = Boolean_Choices(sun_roof)
            bluetooth = Boolean_Choices(bluetooth)
            aux_compatibility = Boolean_Choices(aux_compatibility)
            am_radio = Boolean_Choices(am_radio)
            android_car_play = Boolean_Choices(android_car_play)
            usb_compatibility = Boolean_Choices(usb_compatibility)
            wireless_charger = Boolean_Choices(wireless_charger)
            abs = Boolean_Choices(abs)
            ebd = Boolean_Choices(ebd)
            anti_theft_device = Boolean_Choices(anti_theft_device)
            rear_parking_camera = Boolean_Choices(rear_parking_camera)
            lock_sensor = Boolean_Choices(lock_sensor)
            vehicle_certificate = Boolean_Choices(vehicle_certificate)
            accidental = Boolean_Choices(accidental)
            finance = Boolean_Choices(finance)
            extended_warranty = Boolean_Choices(extended_warranty)
            rear_parking_sensor = Boolean_Choices(rear_parking_sensor)
            exchange = Boolean_Choices(exchange)
            try:
                a = CarVariant.objects.get(id=car_variants)
                
            except:
                error_message = ""
                if 'Dealer' in group_list:
                    messages.warning(request, "Please Fill tha Car Details")
                    return HttpResponseRedirect('/dealer/add_car/')
                else:
                    messages.warning(request, "Please Fill tha Car Details")
                    return HttpResponseRedirect('/add_car/')

            data = {'variant': a, 'car_year': car_year,
                    'ownership': ownership, 'total_km_driven': total_km_driven, 'color': car_color, 'fuel_type': fuel_type,
                    'transmission': car_transmission, 'total_keys': total_keys, 'engine_capacity': engine_capacity,
                    'insurance_type': insurance_type, 'insurance_validity': insurance_validity,
                    'fitness_validity': fitness_validity, 'pollution_validity': pollution_validity,
                    'registration_place': registration_place, 'registration_no': registration_no,
                    'demand_price': demand_price, 'power_steering': power_steering, 'cruise_control': cruise_control,
                    'navigation_system': navigation_system, 'adjustable_steering': adjustable_steering,
                    'adjustable_orvm': adjustable_orvm, 'steering_control': steering_control,
                    'air_conditioning': air_conditioning,
                    'power_window': power_window, 'alloy_wheel': alloy_wheel, 'sun_roof': sun_roof,
                    'bluetooth': bluetooth,
                    'aux_compatibility': aux_compatibility, 'am_fm_radio': am_radio, 'android_car_play': android_car_play,
                    'usb_compatibility': usb_compatibility, 'wireless_charger': wireless_charger, 'abs': abs,
                    'rear_parking_sensor': rear_parking_sensor, 'ebd': ebd, 'lock_system': lock_sensor,
                    'anti_theft_device': anti_theft_device, 'total_air_bag': total_air_bag,
                    'rear_parking_camera': rear_parking_camera,
                    'battery_status': battery_status, 'vehicle_warranty': vehicle_certificate,
                    'vehicle_warranty_date': vehicle_certificate_validity, 'tyre_condition': tyre_condition,
                    'accidental': accidental, 'finance': finance, 'extended_warranty': extended_warranty,
                    'exchange': exchange, 'description': description, 'is_active': True}
            # data = {'variant': a, 'car_year': car_year,
            #         'ownership': ownership, 'total_km_driven': total_km_driven}
            data = convert_empty_to_none(data)
            # print('data = ', data)
            try:
                print('dskfndsnf')
                car_details_instance = CarDetails.objects.filter(id=car_id)
                car_details_instance.update(**data)
                if files:
                    car_detail = car_details_instance.last()
                    print('car_detail 11233 = ', car_detail)
                    for file in files:
                        CarImage.objects.create(car_detail=car_detail, image=file, name=file.name, is_active=True, created_by=user)
                        print('car_image = ', file)
            except ValidationError as e:
                print('ndsndfsn')
                # Handle validation errors
                error_message = "Validation error: " + ", ".join(e.messages)
                print('error_message = ', error_message)
            messages.info(request, "Car Edit Successfully")
            return redirect(request.get_full_path())
            # if 'Dealer' in group_list:
            #     return HttpResponseRedirect('/dealer/car_list/')
            # else:
            #     return HttpResponseRedirect('/profile/')
        else:
            return render(request, "Customer/edit_car/edit_car.html", {'car_brands': car_brand, 'car_detail': car_detail,
                                                                     'car_models': car_model,
                                                                     'car_variants': car_variant})
    else:
        return HttpResponseRedirect('/')



def delete_car(request, car_id):
    if request.user.is_authenticated:
        user = request.user
        CarDetails.objects.filter(id=car_id).update(is_active=False)
        messages.warning(request, "Car Delete Successfully !!")
        referrer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referrer)
    else:
        return HttpResponseRedirect('/')
        
        
def View_Customer_Car(request):
    if request.user.is_authenticated:
        user = request.user
        group_list = user.groups.values_list('name', flat=True)
        car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
        all_car_detail = CarDetails.objects.filter(is_active=True).exclude(created_by=user).annotate(car_image=Subquery(car_image))
        if 'Dealer' in group_list:
            return render(request, "Dealer/product/customer_car.html", {'all_car_detail': all_car_detail})
        else:
            return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/')
        

def import_data_from_csv():
    file_path = 'static/csv/car_list_sheet.csv'
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Create a new object of your model and populate fields
            print('row = ', row)
            car_brand_instance = CarBrands.objects.filter(name=row['brand_name'])
            print('car_brand_instance = ',car_brand_instance)
            if not car_brand_instance.exists():
                obj = CarBrands.objects.create(
                    name=row['brand_name'],
                    is_active=True
                    # Add more fields as needed
                )
                print('obj = ', obj)
                # obj.save()
            brand_instance = CarBrands.objects.filter(name=row['brand_name'], is_active=True)
            car_model_instance = CarModel.objects.filter(name=row['model_name'], is_active=True, brand=brand_instance.last())
            print('car_model_instance = ', car_model_instance)
            if not car_model_instance.exists():
                obj2 = CarModel.objects.create(name=row['model_name'], is_active=True, brand=brand_instance.last())
                print('obj2 = ', obj2)
                # obj2.save()
            car_model_instance = CarModel.objects.filter(name=row['model_name'], is_active=True)
            print('car_model_instance = ', car_model_instance)
            car_variant_instance = CarVariant.objects.filter(name=row['variant_name'], is_active=True, model=car_model_instance.last())
            if not car_variant_instance.exists():
                obj3 = CarVariant.objects.create(name=row['variant_name'], is_active=True, model=car_model_instance.last())
                print('obj3 = ', obj3)
                # obj3.save()


