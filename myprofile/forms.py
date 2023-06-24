from django import forms
from .models import Enquiry
from django.forms import widgets

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','email','contact','message','content']

    def __init__(self,*args,**kwargs):
        super(EnquiryForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
        self.fields['contact'].widget.attrs.update({'class':'form-control','placeholder':'Mobile'})
        self.fields['message'].widget.attrs.update({'class':'form-control','placeholder':'Regarding'})
        self.fields['content'].widget.attrs.update({'class':'form-control','placeholder':'Message'})