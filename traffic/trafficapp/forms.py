from django import forms
from .models import *

class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields=('fname','email','password','phoneNumber','adrs','District')
        widigets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control'}),
            'gen':forms.TextInput(attrs={'class':'form-control'}),
            'adrs':forms.TextInput(attrs={'class':'form-control'}),
            'District':forms.TextInput(attrs={'class':'form-control'}),
        }

class userform(forms.ModelForm):
    class Meta:
        model=usermodel
        fields=('uname','email','upassword','phoneNumber','adrs','District','vid')
        widigets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'upassword':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control'}),
            'gen':forms.TextInput(attrs={'class':'form-control'}),
            'adrs':forms.TextInput(attrs={'class':'form-control'}),
            'District':forms.TextInput(attrs={'class':'form-control'}),
            'vid':forms.TextInput(attrs={'class':'form-control'}),
        }

class caseform(forms.ModelForm):
    class Meta:
        model=casemodel
        fields=('caseid','casename','discription','location','vehicleno','uname','vehicleownerid','amount','date')
        widigets={
            'caseid':forms.TextInput(attrs={'class':'form-control'}),
            'casename':forms.TextInput(attrs={'class':'form-control'}),
            'discription':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'vehicleno':forms.TextInput(attrs={'class':'form-control'}),
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'vehicleownerid':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control'}),
        }

class ruleform(forms.ModelForm):
    class Meta:
        model=rulemodel
        fields=('ruleid','rule')
        widigets={
            'ruleid':forms.TextInput(attrs={'class':'form-control'}),
            'rule':forms.TextInput(attrs={'class':'form-control'}),
        }

class resultform(forms.ModelForm):
    class Meta:
        model=resultmodel
        fields=('vehicleno',)
        widigets={
            'vehicleno':forms.TextInput(attrs={'class':'form-control'}),
            # 'uname':forms.TextInput(attrs={'class':'form-control'}),
        }
        