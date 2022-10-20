from django import forms
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all_'
        exclude = ('SLug')
