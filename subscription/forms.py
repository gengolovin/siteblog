from django import forms
from .models import Subscription
#from captcha.fields import CaptchaField


class SubscriptionForm(forms.ModelForm):
    ### Форма подписки по email ###
    #captcha = CaptchaField()
    
    class Meta:
        model = Subscription
        fields = ("email",)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "editContent", "placeholder": "Your email..."},)
        }
        
        labels = {
            "email": '',
        }


