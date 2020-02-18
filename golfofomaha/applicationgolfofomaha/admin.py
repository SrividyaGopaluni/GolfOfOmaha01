from __future__ import unicode_literals

from django.contrib import admin

from .models import UserCreated, SlotBooking, Event
from django.utils.safestring import mark_safe
import datetime
import calendar
from django.urls import reverse
from .utils import Event


class CustomerList(admin.ModelAdmin):
    list_display = ( 'user', )
    list_filter = ( 'user', )
    search_fields = ('user', )
    ordering = ['user']


class SlotBookingList(admin.ModelAdmin):
    list_display = ( 'event', 'user')
    list_filter = ( 'event', 'user')
    search_fields = ('user', 'user')
    ordering = ['user', 'user']


class EventList(admin.ModelAdmin):
    list_display = ('title', 'start_date')
    list_filter = ('title', 'start_date')
    search_fields = ('title', 'start_date')
    ordering = ['title', 'start_date']


admin.site.register(UserCreated, CustomerList)
admin.site.register(SlotBooking, SlotBookingList)
admin.site.register(Event)
