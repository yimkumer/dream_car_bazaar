from .views import *
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('dealer_signup/', dealer_signup, name='dealer_signup'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('add_car/', add_car, name='add_car'),
    path('whislist_car/', whislist_car, name='whislist_car'),
    path('order_car/', order_car, name='order_car'),
    path('car_listing/', car_listing, name='car_listing'),
    path('about/', about, name='about'),
    path('our_packages/', our_package, name='our_packages'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('insurance/', insurance, name='insurance'),
    path('profile-details/<str:car_id>/', profile_details, name='profile_details'),
    path('service-level-agreement/', sla, name='sla'),


    # path('my_vehicle/', my_vehicle, name='my_vehicle'),

    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
