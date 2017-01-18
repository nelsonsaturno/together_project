from django import forms
from django.contrib.auth import authenticate, login

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from base_accounts.forms import LoginForm


class CustomLoginForm(LoginForm):
    pass

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            'password',
        )
        self.helper.add_input(Submit('submit', 'Login', css_class='btn-lg'))
