from django import forms

class ApplicationForm(forms.Form):
    # Define fields for the application form here
    pass



from .models import MyImage

class Product(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ['image', 'name', 'description']
