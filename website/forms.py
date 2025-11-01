from django import forms
from website.models import Contact
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False)
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'captcha']