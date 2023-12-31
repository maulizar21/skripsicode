from django.urls import path
from .views import beranda, jadwaltoday,login,absensi,logout_user,jadwalkuliah, konfirmasi_hadir

urlpatterns = [
    path('', beranda, name='beranda'),
    path('login', login, name='loginform'),
    path('absensi', absensi, name='absensi'),
    path('konfirmasi_hadir/<int:presence_id>', konfirmasi_hadir, name='konfirmasi_hadir'),
    path('logout',logout_user , name="logout"),
    path('jadwal_kuliah',jadwalkuliah, name="jadwalkuliah"),
    path('jadwal_today',jadwaltoday, name="jadwaltoday")
]
 