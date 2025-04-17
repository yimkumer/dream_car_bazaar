from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

handler404 = 'Dealer.views.custom_404'
urlpatterns = [
    path('add_car/', add_car, name='add_car'),
    path('car_list/', car_list, name='car_list'),
    path('share/<str:id>/',share_this,name='share_this'),
    path('upload_pdf/',upload_pdf,name='upload_pdf'),
    path('invoice/', invoice_view, name='invoice'),
    path('download/pdf/', download_pdf, name='download_pdf'),
    path('download/excel/', download_excel, name='download_excel'), 
    path('dealer/download/selected_pdf/', download_selected_pdf, name='download_selected_pdf'),
    path('dealer/download/selected_excel/', download_selected_excel, name='download_selected_excel'),
    path('car_detail/<str:id>/', car_detail, name='car_detail'),
    path('customer_car/', customer_car, name='customer_car'),
    path('dealer-profile/', profile, name='dealer-profile'),
    path('insurance/', insurance, name='insurance'),
    path('dashboard/', dealer_dashboard, name='dashboard'),
    path('follow-up/', follow_up_view, name='follow_up'),
    path('notification/read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    path('delete-notification/<int:notification_id>/', delete_notification, name='delete_notification'),
    path('update-lead/<str:car>/', update_lead_status, name='update_lead'),
    path('update-duration/', update_duration, name='update_duration'),
    path('download/lead-excel/', download_lead_excel, name='download_lead_excel'),
    path('warranty/', warranty, name='warranty'),   
    # path('warranty/delete/<str:id>/',delete_warranty, name='delete_warranty'),
    path('warranty/delete/<str:id>/',delete_warranty, name='delete-warranty'),
    path('insurance/delete/<str:id>/',delete_insurance, name='delete-insurance'),    
    path('repost/<str:id>/',repost_ad,name='repost_ad' ),
    path('delete/<str:id>/',delete_ad,name='delete-ad'),
    path('marksold/<str:id>/',marksold,name='marksold'),
    path('markdelete/<str:id>/',markdelete,name='markdelete'),
    path('update-car-detail/<str:id>/', update_car_detail, name='update-car-detail'),
    path('update-interior/<str:id>/',update_interior,name='update-interior'),
    path('update-exterior/<str:id>/',update_exterior,name='update-exterior'),    
    path('update-infotainment/<str:id>/',update_infotainment,name='update-infotainment'),
    path('update-safety/<str:id>/',update_safety,name='update-safety'),
    path('update-vehicle/<str:id>/',update_vehicle,name='update-vehicle'),    
    path('update-additional/<str:id>/',update_additional,name='update-additional'),
    path('update-top/<str:id>/',update_top,name='update-top'),
     path('generate_card/<int:car_id>/', generate_card_view, name='generate_card'),
]

if settings.DEBUG:  # This is important to serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)