from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.widgets.EmailInput({
        'type': 'username',
        'class': 'input',
        'placeholder': 'username',
        'name': 'username',
    }))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          'class': 'input',
                                          'type': 'password',
                                          'placeholder': '********', }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          'class': 'input',
                                          'type': 'password',
                                          'placeholder': '********', }),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    email = forms.CharField(widget=forms.widgets.EmailInput({
        'type': 'email',
        'class': 'input',
        'placeholder': 'e.g. alex@example.com',
        'name': 'email'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user
