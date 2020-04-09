from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class UserCreated(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cust_name = models.CharField("Customer Name", max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserCreated.objects.create(user=instance)



    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)


class Event(models.Model):
    title = models.CharField("Golf Events", max_length=200)
    description = models.TextField("Descirption of event")
    start_time = models.DateField("Date")

    # end_time = models.DateField(default=start_time)

    @property
    def get_html_url(self):
        url = reverse('golfapplication:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return str(self.title)


class SlotBooking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_slot_event', null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_choice')
    timeslot = models.TimeField("Time")
    bookingdate = models.DateField("booking date")

    def __str__(self):
        return str(self.event)



    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()





