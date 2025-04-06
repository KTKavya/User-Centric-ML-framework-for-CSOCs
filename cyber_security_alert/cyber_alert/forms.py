from django import forms

from cyber_alert.models import AdminRegister,GiverTransaction


class AdminForm(forms.ModelForm):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = AdminRegister
        fields = ('adminid', 'name', 'email', 'password', 'phoneno', 'address')

class GiverForm(forms.ModelForm):

    class Meta:
        model = GiverTransaction
        fields = ('userid','name','aadharno','merchant','mobileno','bankname','accountno','category','amount','ifsccode','date','time','transationid','gender','age')
        

