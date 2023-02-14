from django import forms
from django.db import IntegrityError

from core.models import Account


class AddUserForm(forms.ModelForm):
    error_messages = {
        "client_id": "Bu müştəri ID-si ilə artıq müştəri mövcuddur",
        "email": "Bu email ilə artıq müştəri mövcuddur",
    }

    class Meta:
        model = Account
        fields = ['client_id', 'email', 'password']

    def clean_client_id(self):
        client_id = self.cleaned_data.get("client_id", None)
        if Account.objects.filter(client_id=client_id).exists():
            raise forms.ValidationError(self.error_messages["client_id"], code="client_id")
        return client_id

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages["email"], code="email")
        return email
