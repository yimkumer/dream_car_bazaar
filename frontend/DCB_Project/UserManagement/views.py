from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import *
from ProductManagement.models import *
from django.db.models import Exists, F, Subquery, OuterRef, Q

from django.contrib.auth.models import Group
from .templatetags import *
from itertools import chain

# Create your views here.


def home(request):
    form = LoginForm()
    car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
    car_details = CarDetails.objects.filter(is_active=True,review='approved').exclude(is_draft=True).exclude(status='deleted').exclude(status='sold').annotate(car_image=Subquery(car_image)).order_by('-updated_at')[:12]
    draft_live = DraftCarDetails.objects.filter(status='live').exclude(is_draft=True).order_by('-updated_at')
    combined_list = list(car_details) + list(draft_live.exclude(cardetails_ptr_id__in=car_details.values('id')))

    # Removing duplicates in case the car_details are in both the main list and draft list
    combined_list = list(set(combined_list))
    all_car_details = combined_list
    car_brand = CarBrands.objects.filter(is_active=True)
    # print('car_brand = ', car_brand)
    car_model = CarModel.objects.filter(is_active=True)
    car_variant = CarVariant.objects.filter(is_active=True)
    # print('all_car_details = ', all_car_details)
    return render(request, "Website/index.html", {'form': form, 'all_car_details': all_car_details, 'car_brands': car_brand, 'car_models': car_model, 'car_variants': car_variant})


def car_listing(request):
    form = LoginForm()
    car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
    all_car_details = CarDetails.objects.filter(is_active=True,review='approved').exclude(is_draft= True).exclude(status='deleted').exclude(status='sold').annotate(car_image=Subquery(car_image)).order_by('-created_at')
    car_brand = CarBrands.objects.filter(is_active=True)
    # print('all_car_details = ', all_car_details)
    return render(request, "Website/product_details/product_detail.html", {'form': form, 'all_car_details': all_car_details, 'car_brands': car_brand})


def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        password = request.POST.get('password')
        check_user_instance = CustomUser.objects.filter(phone=phone_no)
        if not check_user_instance:
            user = CustomUser.objects.create_user(password=password, email=email, phone=phone_no, is_active=True,
                                                  address=address, first_name=full_name)
            customer_group = Group.objects.get(name='Customer')  # Replace with your group name
            user.groups.add(customer_group)
            print('user = ', user)
            # user.save()
            messages.info(request, "SignUp Successfully")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Mobile No. already exists.")
            return HttpResponseRedirect('/')
    return render(request, "Website/index.html")


def dealer_signup(request):
    current_user = request.user
    print('pspd = ', request.FILES)
    print('request = ', request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        password = request.POST.get('password')
        firm_name = request.POST.get('firm_name')
        pan_card = request.FILES.get('pan_card')
        aadhar_card = request.FILES.get('aadhar_card')
        print('pan_card = ', pan_card)
        user = CustomUser.objects.filter(id=current_user.id)
        user.update(firm_name=firm_name, pan_card=pan_card, first_name=name,
                    email=email, phone=phone_no, address=address,
                    aadhar_card=aadhar_card)
        user_instance = CustomUser.objects.get(id=current_user.id)
        print('user = ', user)
        dealer_group = Group.objects.get(name='Dealer')  # Replace with your group name
        user_instance.groups.add(dealer_group)
        # user.save()
        messages.info(request, "Dealer SignUp Successfully")
        return HttpResponseRedirect('/')
    return render(request, "Website/index.html", {'user': current_user})


def user_login(request):
    if request.method == 'POST':
        # username = request.POST['phone']
        # password = request.POST['password']
        # print('password = ', password, username)
        form = LoginForm(request.POST)
        # print('form == ', form)
        if form.is_valid():
            # print(form.cleaned_data)
            uname = form.cleaned_data['email_or_phone']
            upass = form.cleaned_data['password']
            # user = CustomUser.objects.get(phone=uname)

            if '@' in uname:
                user_instance = CustomUser.objects.filter(email=uname)

            else:
                user_instance = CustomUser.objects.filter(phone=uname)
            
            if user_instance.exists():
                user = user_instance.last()
                uname = user.phone
                if user.is_active:
                    user = authenticate(request, username=uname, password=upass)

                    if user is not None:
                        login(request, user)
                        user_group = user.groups.values_list('name', flat=True)
                        if 'Admin' in user_group:
                            messages.info(request, "Successfully Admin Login")
                            return HttpResponseRedirect('/executive/pending_car_approval/')
                        elif 'Dealer' in user_group:
                            messages.info(request, "Successfully Dealer Login")
                            return HttpResponseRedirect('/')
                        else:
                            messages.info(request, "Successfully Login")
                            return HttpResponseRedirect('/')  # Redirect to a success page after successful login
                    else:
                        # Invalid login credentials
                        print('success')
                        messages.warning(request, "Invalid username or password.")
                        return HttpResponseRedirect('/')
                else:
                    # Invalid login credentials
                    print('inactive user')
                    messages.warning(request, "Your account is Inactive")
                    return HttpResponseRedirect('/')

            else:
                print('kdskfkds')
                messages.warning(request, "Invalid username or password.")
                return HttpResponseRedirect('/')
        else:
            # form = LoginForm()
            messages.warning(request, "Invalid username or password.")
            # print('form = ', form)
            return HttpResponseRedirect('/')

    else:
        print('else')
        return HttpResponseRedirect('/')


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        phone_no = user.phone
        # print('user =  = ', user)
        # print('phone = ', user.phone)
        # login_user = CustomUser.objects.get(username=login_user)
        user_instance = CustomUser.objects.get(phone=phone_no)
        if request.method == 'POST':
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            phone_no = request.POST.get('phone')
            address = request.POST.get('address')
            password = request.POST.get('password')

            user = CustomUser.objects.filter(phone=user.phone)
            user_instance = user.last()
            if password:
                user.update(password=password, email=email, phone=phone_no, is_active=True,
                            address=address, first_name=full_name)
                update_session_auth_hash(request, user_instance)  # for dont updating session after changing password
            else:
                user.update(email=email, phone=phone_no, is_active=True,
                            address=address, first_name=full_name)
            print('user = ', user)
            # user.save()
            messages.info(request, "Profile Edit Successfully")
            return HttpResponseRedirect('/profile/')

        else:
            return render(request, "Customer/profile/profile.html", {'user': user_instance})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    referer = request.META.get('HTTP_REFERER')
    # print(referer)
    logout(request)
    redirect_url = f'/?next={referer}'
    if referer:
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseRedirect('/home/')


def add_car(request):
    if request.user.is_authenticated:
        car_brand = CarBrands.objects.filter(is_active=True)
        car_model = CarModel.objects.filter(is_active=True)
        car_variant = CarVariant.objects.filter(is_active=True)
        if request.method == 'POST':
            return render(request, "Customer/add_car/add_car.html")
        return render(request, "Customer/add_car/add_car.html", {'car_brands': car_brand,
                                                                 'car_models': car_model,
                                                                 'car_variants': car_variant})
    else:
        return HttpResponseRedirect('/')
        


# def edit_car(request, car_id):
#     if request.user.is_authenticated:
#         car_detail = CarDetails.objects.filter(id=car_id).last()
#         car_brand = CarBrands.objects.filter(is_active=True)
#         # print('car_brand = ', car_brand)
#         car_model = CarModel.objects.filter(is_active=True)
#         car_variant = CarVariant.objects.filter(is_active=True)
#         # car_detail = CarDetails.objects.get(id=car_id)
#         if request.method == 'POST':
#             return render(request, "Customer/add_car/add_car.html")
#         return render(request, "Customer/edit_car/edit_car.html", {'car_brands': car_brand, 'car_detail': car_detail,
#                                                                  'car_models': car_model,
#                                                                  'car_variants': car_variant})
#     else:
#         return HttpResponseRedirect('/')


def whislist_car(request):
    if request.user.is_authenticated:
        user = request.user
        wishlist_cars = WishlistCar.objects.filter(wishlist_by=user, is_active=True, is_wishlist=True)
        return render(request, "Customer/whislist_car/whislist_car.html", {'wishlist_cars': wishlist_cars})
    else:
        return HttpResponseRedirect('/')

def order_car(request):
    return render(request, "Customer/order_car/order_car.html")
    

def about(request):
    form = LoginForm()
    return render(request, "Website/about.html", {'form': form})
    

def our_package(request):
    return render(request, "Website/our-package.html")
    

def terms_and_conditions(request):
    return render(request, "Website/terms-and-conditions.html")
    


def privacy_policy(request):
    return render(request, "Website/privacy-policy.html")
    
def insurance(request):
    return render(request, "Website/insurance.html")
    
def sla(request):
    return render(request, "Website/Our_SLA.html")
  
  
def profile_details(request, car_id):
    car_instance = CarDetails.objects.filter(id=car_id)
    if car_instance.exists():
        last_car = car_instance.last()
        car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
        all_car_details = CarDetails.objects.filter(created_by=last_car.created_by).annotate(car_image=Subquery(car_image)).order_by('-created_at')
    
        # all_car_details = CarDetails.objects.filter(created_by=last_car.created_by)
        total_car = all_car_details.count()
        return render(request, "Website/profile-detais.html", {'last_car': last_car, 'total_car': total_car, 'all_car_details': all_car_details})
    else:
        return HttpResponseRedirect('/')
  
 
 
 
   
def utkarsh(request):
    return render(request, "Website/utkarsh-page.php")

# def my_vehicle(request): 
#     return render(request, "Customer/my_vehicle/my_vehicle.html")
