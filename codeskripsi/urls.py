from django.urls import path
from .views import beranda, jadwaltoday,login,absensi,logout_user,jadwalkuliah

urlpatterns = [
    path('', beranda, name='beranda'),
    path('login', login, name='loginform'),
    path('absensi', absensi, name='absensi'),
    path('logout',logout_user , name="logout"),
    path('jadwal kuliah',jadwalkuliah, name="jadwalkuliah"),
    path('jadwal kuliah hari ini',jadwaltoday, name="jadwaltoday")
]
 