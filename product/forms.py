from django import forms
from product.models import Product, Application


class SearchForm(forms.ModelForm):
    title = forms.CharField(max_length=20)


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['company_url', 'short_description', 'company_date','monetize','image','company_address']#'long_description', 'company_zipcode', 'company_place', 'company_country', 'company_size']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']