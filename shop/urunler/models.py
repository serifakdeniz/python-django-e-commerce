from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class kategoriler(models.Model):
    isim=models.CharField(max_length=155)
    ustkategori=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,help_text="eğer başka bir kategoriye bağlıysa burayı doldurunuz")
    aktifmi=models.BooleanField(default=True)

    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=155,unique=True,null=True,blank=True)

    
    class Meta:
        verbose_name_plural="kategoriler"
        verbose_name="kategori"

    def __str__(self):
        return self.isim
    

class Markalar(models.Model):
    isim=models.CharField(max_length=155)
    aciklama=models.TextField(blank=True,null=True)
    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=155,unique=True,blank=True,null=True)
    aktifmi=models.BooleanField(default=True)
    resim=models.ImageField(upload_to="markaresimleri",blank=True,null=True)

        
    class Meta:
        verbose_name_plural="Markalar"
        verbose_name="Marka"
    def __str__(self):
        return self.isim
    

class Urunler(models.Model):
    isim=models.CharField(max_length=155)
    kullanici=models.ForeignKey(User,on_delete=models.CASCADE)
    fiyat=models.DecimalField(max_digits=10,decimal_places=2)
    marka=models.ForeignKey(Markalar,on_delete=models.CASCADE)
    kategori=models.ForeignKey(kategoriler,on_delete=models.CASCADE)
    indirimli_fiyat=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    kisa_aciklama=models.TextField(blank=True,null=True)
    aciklama=models.TextField(blank=True,null=True)
    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=155,unique=True,blank=True,null=True)
    aktifmi=models.BooleanField(default=True)
    resim=models.ImageField(upload_to="markaresimleri",blank=True,null=True)
    tarih=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural="Ürünler"
        verbose_name="Ürün"
    def __str__(self):
        return self.isim
    


