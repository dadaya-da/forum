from django import forms
class AddNewPost(forms.Form):
    post_name = forms.CharField(max_length=50)
    post_text = forms.CharField(max_length=200)
class AddNewComment(forms.Form):
    comment_text = forms.CharField(max_length=200, label='', widget=forms.Textarea, required = False)
    post = forms.IntegerField(widget=forms.HiddenInput, required = False)
class Search(forms.Form):
    search_text = forms.CharField(max_length=50, widget=forms.TextInput)
