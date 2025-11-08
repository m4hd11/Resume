from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    subject = forms.CharField(required=False)
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message']