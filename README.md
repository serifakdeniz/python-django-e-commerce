"# python-django-e-commerce" 
py -m venv eteticaret

eteticaret\Scripts\activate.bat

pip install django

cd eteproject

django-admin startproject shop

cd shop 

python manage.py runserver


python manage.py migrate    (veritabanında tabloları oluşturmak için migrate etmek gerekiyor bu komut bir işe yarıyor)


python manage.py createsuperuser    (  bu komut admin superuser oluşturmamıza yarıyor.bunu oluşturduktan sonra diğerlerini oluşturu.)

python manage.py startapp urunler     (yeni bir uygulama oluşturmak için bu komut kullanılır)

urunler i settings.py içine app olarak eklemek gerekiyor

python manage.py makemigrations  (kategoriler diye bir   model class oluşturduk models.py içinde sonra bu komut ile gerekli sqller oluştu)
Migrations for 'urunler':
  urunler\migrations\0001_initial.py
    + Create model kategoriler


(yteticaret) C:\yteticaret\shop>python manage.py migrate   (makemigration dedikten sonra migrate komutu hep girilir.)
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, urunler
Running migrations:
  Applying urunler.0001_initial... OK




SONRA urunler.admins.py içine aşağdıkai kod eklendi admin kısmından kategorileri görmek için yapıldı.
from .models import kategoriler
# Register your models here.
admin.site.register(kategoriler)


sonra admin kısmından kategoriler kısmı seçilip kategori eklenir örnek diğer kozmetik giib.
ama bir sorun var isimler burdaki gibi gelmedi kategori 1 2 falan yazıyor.
bunun için çözüm şu şekilde


sonra yine models.py içine aşağıdaki giib bir kod ekledik çünkü kategorilers olarak çoğul geliyprdu
    class Meta:
        verbose_name_plural="Kategoriler"
        verbose_name="Kategori"



sonra bu kategorinin üst kategorisini belirlemek için aşğıdaki kodu models.py e ekledik

    ustkategori=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,help_text="eğer başka bir kategoriye bağlıysa burayı doldurunuz")

makemigrations ve migrate yaptıktan sonra görüntüledik..



daha sonra aşağıdaki kodları models.py içine ekledik.

class Markalar(models.Model):
    isim=models.CharField(max_length=155)
    aciklama=models.TextField(blank=True,null=True)
    seo_title=models.CharField(max_length=155,blank=True,null=True)
    seo_description=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=155,unique=True,null=True,blank=True)
    aktifmi=models.BooleanField(default=True)
    resim=models.ImageField(upload_to="markaresimleri",blank=True,null=True)


sonra image kısmından dolayı hata veriyor,
bunun için 
pip install pillow kütüphanesii yüklüyoruz .

pythonda projemde hangi paketleri yüklemişim diye aşağıdaki komut girilir.

pip freeze > requirements.txt

komutu kullanılır.


DAHA SONRA  settings.py içine aşağıdaki kod eklendi resim yükleme için
MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR / 'media'

sonra urls.py içine aşağıdaki kod eklendi

+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

