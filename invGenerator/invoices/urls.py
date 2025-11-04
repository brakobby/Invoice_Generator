from . import views
from django.urls import path

urlpatterns = [
    path('',views.renderPage, name='home'),
    path('dashboard/',views.dashBoardView, name="dashboard"),
    path('invoice/', views.invoice_portal, name='invoice'),
    path('new_invoice/', views.newInvoice, name='new_invoice'),
    path('customer/', views.customer, name='customer'),
    path('report/', views.reports, name='report'),
    path('setting/', views.settings, name='setting')
]

