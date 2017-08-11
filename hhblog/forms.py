from django import forms
from . models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def __init__(self,  *args, **kwargs):
        super(EmailPostForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['to'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Friends Email'})
        self.fields['comments'].widget.attrs.update({'class': 'form-control message input-message',
                                            'placeholder': 'Message'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

    def __init__(self,  *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['body'].widget.attrs.update({'class': 'form-control message input-message',
                                                    'placeholder': 'Leave a comment.'})
