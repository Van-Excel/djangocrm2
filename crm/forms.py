from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    email= forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email address'}))

    class Meta:
        model = User

        # choose fields we want to display as well as extend User default fields
        fields = ('username', 'first_name', 
                  'last_name','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):

        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password must contain at least 8 characters.</li>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddRecord(ModelForm):

    first_name = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email= forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email address', 'class': 'form-control'}))
    address = forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    city = forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode= forms.CharField(label='',required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'ZipCode', 'class': 'form-control'}))

    class Meta:
        model = Record
        exclude = [ 'created_at']




    
       


		
		
        

		
			

		
		
		                 
		

		
    