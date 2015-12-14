from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.widgets import AdminDateWidget
from traceapp.models import UserReg
from django.contrib.auth.models import User

#New User Registration Form
class UserRegistrationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)
		#self.fields['loan_date'].widget.attrs['class'] = 'calendar'
	class Meta:
		model = UserReg
		fields = ['first_name', 'last_name', 'email', 'username', 'password']
		#widgets = {'asset': forms.HiddenInput(), 'applicant': forms.HiddenInput(), 'status': forms.HiddenInput(), 'reservation_date': forms.HiddenInput()}

