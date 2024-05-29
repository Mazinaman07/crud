from django import forms 
from . models import *



class itemform(forms.ModelForm):
    class Meta:
        model = itemsmodel
        fields = '__all__'

class userform(forms.ModelForm):
    class Meta:
        model = usermodel
        fields = '__all__'



