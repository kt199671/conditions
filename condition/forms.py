from django import forms
from .models import Condition
from django.contrib.auth import get_user_model

User = get_user_model()


class PostForm(forms.Form):
    temperature = forms.DecimalField(max_digits=3, decimal_places=1, initial=36.5)
    conditioning = forms.BooleanField(label='sick', required=False)
    content = forms.CharField(max_length=500, required=False,\
                              help_text='Fill in if you or your families are not feeling well.',\
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

class CondForm(forms.ModelForm):
# ModelFormを継承
    class Meta:
        model = Condition
        fields = ('temperature','conditioning','content')
