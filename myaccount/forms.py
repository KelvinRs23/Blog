from django import forms

from myaccount.models import Category, Film


class PostForm(forms.Form):
    Nama = forms.CharField(max_length = 100)
    Komentar = forms.CharField(
        widget = forms.Textarea
    )

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['judul', 'deskripsi', 'kategori', 'image']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan judul film.html'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deskripsi film.html'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'judul': 'Judul Film',
            'deskripsi': 'Deskripsi Film',
            'kategori': 'Kategori Film',
            'image': 'Upload Gambar',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nama']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama kategori'}),
        }
        labels = {
            'nama': 'Nama Kategori',
        }