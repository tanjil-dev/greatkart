from typing import Any, Dict
from django import forms
from .models import Account

class RegistartionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type password','class':'form-control',}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        # 'class':'form-control',
        })) 

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    def clean(self):
        cleaned_data     = super(RegistartionForm,self).clean()
        password         = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self,*args,**kwargs):
        super(RegistartionForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter fisrt name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter last name'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter phone number                                                                                         '
        self.fields['email'].widget.attrs['placeholder']='Enter email'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    
class UserForm(forms.ModelForm):
    class Meta:
        model  = Account()
        fields = ('first_name','last_name','phone_number')
        
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

# class UserProfileForm(forms.ModelForm):
#     profile_picture = forms.ImageField(required=False,error_messages={'invalid':("Image Files Only")},widget=forms.FileInput)
#     class Meta:
#         model  = UserProfile()
#         fields = ('address_line_1','address_line_2','city','province','country','profile_picture')
#     def __init__(self,*args,**kwargs):
#         super(UserProfileForm,self).__init__(*args,**kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class']='form-control'
        