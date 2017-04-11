from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self,  *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['contact_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contact Email'})
        self.fields['content'].widget.attrs.update({'class': 'form-control message input-message',
                                                    'placeholder': 'Get in touch with us.'})


class AxesCaptchaForm(forms.Form):
    captcha = CaptchaField()




