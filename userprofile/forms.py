from django import forms

from .models import Userprofile

class AddSellerForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        
        fields = ['profile_pic','user', 'is_seller', 'is_agree','phone','secondary_phone','address','country','city','state','zipcode',]
