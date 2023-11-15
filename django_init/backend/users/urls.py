from users.views.v1.user_registration_view import CustomerRegistrationView
from users.views.v1.user_auth_view import CustomerAuthView
from django.urls import path


urlpatterns = [
    path("registration/", CustomerRegistrationView.as_view(), name="customer_registration"),
    path("auth/", CustomerAuthView.as_view(), name="customer_auth"),
]
