from django import forms
    
class NewPageForm(forms.Form):
     title   = forms.CharField(help_text="enter a title", required=True)
     content = forms.CharField(required=True)

class EditEntryForm(forms.Form):
    title   = forms.CharField(help_text="Edit a title", required=True)
    content = forms.CharField(required=True)