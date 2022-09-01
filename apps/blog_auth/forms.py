from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1: forms.CharField(max_length=70, widget=forms.PasswordInput)
    password2: forms.CharField(max_length=70, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        help_texts = {k:"" for k in fields }

    def clean(self):
        '''Verifico que las contrasenias sean iguales'''
        data  = super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Las contrasenias no coinciden")

        return data