
#encoding: UTF-8

from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'type':'email','id':'email', 'class':'validate'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'id':'message', 'class':'materialize-textarea'}))