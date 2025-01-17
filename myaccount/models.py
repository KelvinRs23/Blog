from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    KATEGORI = (
            (' Horror Indo & Horror Luar Negri','Horror Indo & Horror Luar Negri'),
            (' Comedy Indo & Comedy Luar Negri ', ' Comedy Indo & Comedy Luar Negri '),
            (' Romance Indo & Romance Luar Negri', 'Romance Indo & Romance Luar Negri'),
            )
    nama = models.CharField(max_length=1000) 
    desk = models.TextField(max_length=1000, null=True)
    deskripsi = models.TextField()
    kategori = models.CharField(max_length=1000, null=True, choices=KATEGORI)
    image = models.ImageField(upload_to='static/%y')
    tags = models.ManyToManyField(Tag)
    button = models.CharField(max_length=1000, null=True) 

    def __str__(self): 
        return self.nama

class Comment(models.Model):
    Nama = models.CharField(max_length=1000)
    Komentar = models.TextField()

    def __str__(self): 
        return self.Nama

class Category(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Film(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    #image = models.ImageField()
    image = CloudinaryField('image')
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)