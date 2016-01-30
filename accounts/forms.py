from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def save(self,commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class SignupForm2(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = ['username','email']

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer !=6:
            raise forms.ValidationError("땡!!!")
        return answer
