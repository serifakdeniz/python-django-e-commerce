from django.contrib import admin
from .models import kategoriler,Markalar,Urunler
# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
    list_display=['isim','seo_title','slug','aktifmi']
    list_filter=['aktifmi']
    search_fields=['isim','seo_title','slug']

admin.site.register(kategoriler,KategoriAdmin)


class MarkalarAdmin(admin.ModelAdmin):
    list_display=['isim','seo_title','slug','aktifmi','resim']
    list_filter=['aktifmi','isim']
    search_fields=['isim','seo_title','slug']
admin.site.register(Markalar,MarkalarAdmin)


class UrunlerAdmin(admin.ModelAdmin):
    list_display=['isim','fiyat','marka','kategori','indirimli_fiyat','seo_title','aktifmi','resim','tarih']
    list_filter=['aktifmi','isim','kategori','marka']
    search_fields=['isim','seo_title','slug']
admin.site.register(Urunler,UrunlerAdmin)
    