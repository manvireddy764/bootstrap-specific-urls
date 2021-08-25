from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('mdb_boot_s/',mdb_boot_s,name='mdb_boot_s'),
]