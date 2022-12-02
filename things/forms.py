from django import forms

# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label = "name")
    description = forms.CharField(label = "description", widget = forms.Textarea())
    quantity = forms.IntegerField(label = "quantity", widget = forms.NumberInput())
