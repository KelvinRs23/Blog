from django import forms

class PostForm(forms.Form):
    Nama = forms.CharField(max_length = 100)
    Komentar = forms.CharField(
        widget = forms.Textarea
    )

