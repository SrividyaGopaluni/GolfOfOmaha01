from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .utils import Calendar
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.safestring import mark_safe
from django.db.models import Sum
import calendar


@login_required
def house(request):
    #return render(request,'golfapplication/house.html',{'golfapplication': house})
    slotbook = SlotBooking.objects.filter(user=request.user)
    event = Event.objects.filter()
    return render(request, 'golfapplication/house.html',
                  {'menu_choices': slotbook, 'events': event})



@login_required
def edit_account(request):
    return render(request, 'golfapplication/edit_account.html', )


@login_required
def contactus(request):
    return render(request, 'golfapplication/contactus.html', )


@login_required
def menu_choice_error(request):
    return render(request, 'golfapplication/menu_choice_error.html', )


#def login(request):
 #   return render(request, 'registration/login.html')


#def password_reset(request):
 #   return render(request, 'registration/password_reset_form.html')




#def logout(request):
#    return render(request, 'golfapplication/templates/registration/logout.html', )


#class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'golfapplication/signup.html'


def staff_main(request):
    return render(request, 'golfapplication/staff_main.html', )


@login_required
def book_slot_new(request):
    try:
        if request.method == "POST":
            form = SlotbookingForm(request.POST)
            if form.is_valid():
                menuchoice = form.save(commit=False)
                menuchoice.user = request.user
                menuchoice.save()
                menu_choice = SlotBooking.objects.filter(user=request.user)
                return render(request, 'golfapplication/house.html',
                              {'menu_choices': menu_choice})
        else:
            form = SlotbookingForm()
            # print("Else")
    except (IntegrityError, UnboundLocalError):
        return render(request, 'golfapplication/menu_choice_error.html')
    return render(request, 'golfapplication/menu_choice_new.html', {'form': form})

@login_required
def book_slot_edit(request, pk):
    menuchoice = SlotBooking.objects.filter(pk=pk).first()
    if request.method == "POST":
        form = SlotbookingForm(request.POST, instance=menuchoice)
        if form.is_valid():
            menuchoice = form.save()
            menuchoice.user = request.user
            menuchoice.save()
            menu_choice = SlotBooking.objects.filter(user=request.user)
            return render(request, 'golfapplication/house.html',
                          {'menu_choices': menu_choice})
    else:
        # print("else")
        form = SlotbookingForm(instance=menuchoice)
    return render(request, 'golfapplication/book_slot_edit.html', {'form': form})


@login_required
def slot_booking_delete(request, pk):
    deleteslotbooked = SlotBooking.objects.filter(pk=pk).first()
    print(deleteslotbooked)
    deleteslotbooked.delete()
    return redirect('golfapplication:house')



class CalendarView(generic.ListView):
    model = Event
    template_name = 'golfapplication/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

