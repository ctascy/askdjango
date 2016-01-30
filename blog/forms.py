from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    is_agree = forms.BooleanField(label="약관동의",required=True, error_messages={
    'required': '약관동의필수',
    })
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['message', 'image']
