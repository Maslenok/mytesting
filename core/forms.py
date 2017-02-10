from django.forms import ModelForm
from core.models import User



class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'desc', 'email',)