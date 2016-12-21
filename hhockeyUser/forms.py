from django import forms

from oscar.apps.customer.forms import UserForm as BaseUserForm
from oscar.core.compat import existing_user_fields, get_user_model

User = get_user_model()


class UserForm(BaseUserForm):
    class Meta:
        model = User
        fields = existing_user_fields(['first_name', 'last_name', 'email', 'birth_date', 'league', 'position'])