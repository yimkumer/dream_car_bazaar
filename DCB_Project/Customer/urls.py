from django.urls import path, include
from .views import *

urlpatterns = [
    path('my_vehicle/', my_vehicle, name='my_vehicle'),
    path('car_detail/<str:id>/', car_detail, name='car_details'),
    path('report-spam/', mark_spam, name='mark_spam'),

]
