from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=25)
    password = forms.CharField(label="password", max_length=25, widget=forms.PasswordInput)


class NoteForm(forms.Form):
    noteId = forms.IntegerField(required=False)
    title = forms.CharField(max_length=50, required=False)
    text = forms.CharField(widget=forms.Textarea, max_length=5000, required=False)
