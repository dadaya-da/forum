from django import forms
class AddNewPost(forms.Form):
    post_name = forms.CharField(max_length=50)
    post_text = forms.CharField(max_length=200)
class AddNewComment(forms.Form):
    comment_text = forms.CharField(max_length=200)