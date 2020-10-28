from django.urls import path

from . import views
urlpatterns = [
    path('ho/',views.view1, name='home'),
    path('ac/', views.addCustomer, name='addcustomer'),
    path('sc/', views.all_customer, name='allcustomer'),
    path('acdf/', views.addcust, name='addcustomerdf'),
    path('aodf/', views.addorder, name='addorderdf'),
    path('socf/', views.all_order, name='allorderdf')

]