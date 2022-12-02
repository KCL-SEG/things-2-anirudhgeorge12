from django import forms

# Create your forms here.

class ThingForm(forms.Form):
    name = forms.TextField(label = "name")
    description = forms.TextField(label = "description", widget = forms.Textarea())
    quantity = forms.IntegerField(label = "quantity", widget = forms.NumberInput())
