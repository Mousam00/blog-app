from django import forms
from app.models import Comments,Subscribe
from django.utils.translation import gettext_lazy as __

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields={'content','email','name','website'}
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Type your comment .....'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['website'].widget.attrs['placeholder'] = 'Website (optional)'

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        lable= {'email':__('')}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'