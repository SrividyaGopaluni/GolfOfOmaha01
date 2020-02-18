from django.conf.urls import url
from . import views
from django.urls import path, re_path


app_name = 'golfapplication'
urlpatterns = [
    path('', views.house, name='house'),
    path('house',views.house, name='house'),


    path('edit_account', views.edit_account, name='edit_account'),
    path('contactus', views.contactus, name='contactus'),
    #path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    #path('password_reset', views.password_reset, name='password_reset'),
    #path('signup/', views.SignUp.as_view(), name='signup'),


    path('book_slot_new', views.book_slot_new, name='book_slot_new'),
    path('bookaslot/<int:pk>/delete/', views.slot_booking_delete, name='slot_booking_delete'),
    path('bookaslot/<int:pk>/edit/', views.book_slot_edit, name='book_slot_edit'),





    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),

]
