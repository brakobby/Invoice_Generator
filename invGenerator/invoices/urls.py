from . import views
from django.urls import path


urlpatterns = [
    path('',views.renderPage, name='home'),
    path('invoice/',views.dashBoardView, name="dashboard")
]