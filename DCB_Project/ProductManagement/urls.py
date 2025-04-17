from django.urls import path, include
from .views import *

urlpatterns = [
    path('get_car_model/', get_car_model, name='get_car_model'),
    path('get_car_variant/', get_car_variant, name='get_car_variant'),
    path('save_car/', save_car, name='save_car'),
    path('save_draft/', save_draft, name='save_draft'),
    path('make-live/<str:draft_id>/', make_live, name='make_live'),
    path('resume_form/<str:car_id>/', resume_form, name='resume_form'),
    # path('resume-car-details/<str:car_id>/', resume_car_details, name='resume_car_details'),
    path('wishlist_car/<str:car_id>/', wishlist_car, name='wishlist_car'),
    path('view_car/', view_car, name='view_car'),
    path('website_car_filter/', website_car_filter, name='website_car_filter'),
    path('edit_car/<str:car_id>/', edit_car, name='edit_car'),
    path('delete_car/<str:car_id>/', delete_car, name='delete_car'),
    # path('get-draft-details/<str:draft_id>/', draft_details, name='draft_details'),
    
    # path('get-car-models/<str:brand_id>/', get_car_models, name='get-car-models'),

]
