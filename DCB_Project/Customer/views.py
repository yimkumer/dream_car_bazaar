from django.shortcuts import render
from ProductManagement.models import *
from UserManagement.models import *
from django.db.models import Exists, F, Subquery, OuterRef, Q


# Create your views here.


def my_vehicle(request):
    if request.user.is_authenticated:
        user = request.user
        car_image = CarImage.objects.filter(car_detail=OuterRef('id')).order_by('-created_at').values('image')[:1]
        all_car_details = CarDetails.objects.filter(created_by=user, is_active=True).annotate(car_image=Subquery(car_image)).order_by('-created_at')
        return render(request, "Customer/my_vehicle/my_vehicle.html", {'all_car_details': all_car_details})
    else:
        return HttpResponseRedirect('/')


def car_detail(request, id):
    user = request.user
    car_details = CarDetails.objects.filter(id=id).last()
    car_images = CarImage.objects.filter(car_detail=car_details, is_active=True)
    print('car_details = ', car_details)
    return render(request, "Website/product/car_details.html", {'car_details': car_details, "car_images": car_images})

# def mark_spam(request,id):
#     user = request.user
#     judges = []
#     car = CarDetails.objects.filter(id=id)
    
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SpamReport  # Assuming you have a model to store spam reports
from collections import Counter

@login_required  # Ensure the user is logged in
def mark_spam(request):
    user = request.user
    car_details = CarDetails.objects.filter(id=id).last()
    car_images = CarImage.objects.filter(car_detail=car_details, is_active=True)
    if request.method == 'POST':
        draft_id = request.POST.get('draft_id')  # Get draft ID from form
        remark = request.POST.get('remark')  # Get remark from form

        # Check if the user has already reported this draft
        if SpamReport.objects.filter(user=request.user, draft_id=draft_id).exists():
            return HttpResponse("<h1>You have already reported this draft.</h1>")

        # Save the report to the database
        report = SpamReport.objects.create(user=request.user, draft_id=draft_id, remarks=remark)

        # Check how many unique users have reported this draft
        unique_users_count = SpamReport.objects.filter(draft_id=draft_id).values('user').distinct().count()

        if unique_users_count >= 5:
            # Mark the draft as spam
            # You can implement logic to mark the draft here, e.g., update a field in the draft model
            
            # Determine the primary remark with the highest count
            remarks_count = Counter(SpamReport.objects.filter(draft_id=draft_id).values_list('remarks', flat=True))
            primary_remark = remarks_count.most_common(1)[0] if remarks_count else None
            
            # Handle the logic to update the draft with the primary remark, e.g., 
            draft_object = get_object_or_404(DraftCarDetails, id=draft_id)
            draft_object.is_spam = True
            draft_object.status = 'spam'
            draft_object.primary_remark = primary_remark[0]  # Set the primary remark
            draft_object.save()

            return render(request, "Website/product/car_details.html", {'car_details': car_details, "car_images": car_images}) # Redirect to a success page

        return render(request, "Website/product/car_details.html", {'car_details': car_details, "car_images": car_images})  # Redirect to a success page

    return HttpResponse("<h1>Invalid request method.</h1>")
