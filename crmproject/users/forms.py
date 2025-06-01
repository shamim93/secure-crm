from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Order

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove 'superadmin' from the choices in the registration form
        self.fields['user_type'].choices = [
            choice for choice in self.fields['user_type'].choices
            if choice[0] != 'superadmin'
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','phone','address']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'amount']
class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']