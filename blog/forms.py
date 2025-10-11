from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    subject = forms.CharField(required=False)
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']