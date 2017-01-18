from base_accounts.views import LoginFormView
from accounts.forms import CustomLoginForm


class CustomLoginFormView(LoginFormView):
    form_class = CustomLoginForm
    # form_class = LoginForm
    # template_name = 'base_accounts/login.html'
    # success_url = getattr(settings, 'BASE_ACCOUNTS_LOGIN_REDIRECT_URL', settings.LOGIN_REDIRECT_URL)
    # success_message = _("You have logged in")

    # def get_form_kwargs(self):
    #     """Form uses request to login"""
    #     kwargs = super(LoginFormView, self).get_form_kwargs()
    #     kwargs.update({'request': self.request})
    #     return kwargs
