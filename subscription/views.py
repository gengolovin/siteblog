from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from .models import Subscription
from .forms import SubscriptionForm

class SubscriptionView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    success_url = "/"


    def form_invalid(self, form):
        messages.add_message(self.request,messages.WARNING,"Not a valid email address.")
        return redirect('home')

  