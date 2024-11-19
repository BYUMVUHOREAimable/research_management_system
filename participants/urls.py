from django.urls import path
from .views import participant_list

urlpatterns = [
    path('', participant_list, name='participant_list'),
]
