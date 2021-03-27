from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    CHOICES = (
        ('OL', 'OL'),
        ('TE/FB', 'TE/FB'),
        ('QB', 'QB',),
        ('WR', 'WR'),
        ('RB', 'RB'),
        ('DL', 'DL'),
        ('LB', 'LB'),
        ('DB', 'DB'),
        ('K/P', 'K/P'),
        ('MANAGER', 'MANAGER'),
        ('TRAINER', 'TRAINER'),
        ('COACH', 'COACH'),
    )
    position = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password1')
        retyped = self.cleaned_data.get('password2')
        if password and retyped and (password != retyped):
            self.add_error('password2', 'This does not match with the above.')

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')
        position = self.cleaned_data.get('position')
        new_user = User.objects.create_user(username=username, position=position)
        new_user.set_password(password)
        new_user.save()

    class Meta:
        model = User
        fields = ('username', 'position', 'password1', 'password2')



class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                                max_length=30,
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'User name'
                                    }
                                ),)
    
    password = forms.CharField(required=True,
                                max_length=255,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Password'
                                    }
                                ))
 
 
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if 'username' and 'password' in cleaned_data:
            auth_result = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if not auth_result:
                raise ValidationError('Wrong username or password')
        return cleaned_data
 
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
 
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
