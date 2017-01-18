from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from base_accounts import views as base_accounts_views
from accounts import views as accounts_views


urlpatterns = [
    url(r'^login/$', accounts_views.CustomLoginFormView.as_view(), name='login'),
    url(r'^logout/$', login_required(base_accounts_views.LogoutView.as_view()), name='logout'),
]
