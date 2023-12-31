# AYIIIIIIII
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from codeskripsi.models import Presence
import face_recognition
import io, base64
import os
from PIL import Image
from django.http import JsonResponse
from datetime import datetime, date
from django.utils import timezone
# from PIL import Image
# from base64 import decodestring
# from django.core.files.base import ContentFile
# Create your views here.

def beranda(request):
      
    # render function takes argument  - request
     # and return HTML as response
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('loginform')

def login(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        password = request.POST['password']
        camera_data = request.POST['camera_data']

        user = auth.authenticate(username=nim, password=password)

        if user is not None:
            #simpan gambar dari camera ke server
            img = Image.open(io.BytesIO(base64.decodebytes(bytes(camera_data.split("data:image/jpeg;base64,")[-1], "utf-8"))))
            img.save(os.path.abspath(f'codeskripsi/face_recog/image_temp/{nim}.jpeg'))

            # load gambar yang dari server ke ml
            known_image_dir = f'codeskripsi/face_recog/user_images/{nim}.jpeg'
            unknown_image_dir = f'codeskripsi/face_recog/image_temp/{nim}.jpeg'
            known_image = face_recognition.load_image_file(os.path.abspath(known_image_dir))
            unknown_image = face_recognition.load_image_file(os.path.abspath(unknown_image_dir))

            if(len(face_recognition.face_encodings(unknown_image)) == 0):
                data = {
                    'status' : False,
                    'message' : 'Tidak Ada Wajah Terdeteksi',
                }
                return JsonResponse(data)

            # bandingkan data kamera ke database
            user_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            results = face_recognition.compare_faces([user_encoding], unknown_encoding)
            if(results[0]) :
                
                data = {
                    'status' : True,
                    'message' : 'Masuk'
                }

                auth.login(request, user)
                user_data = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'email': user.email,
                }
                request.session['user_data'] = user_data

                user = User.objects.get(username=user_data['username'])
                current_datetime = datetime.now()
                user_schedule = Presence.objects.filter(
                    user = user,
                    schedule__lte=current_datetime,
                    schedule_limit__gte=current_datetime,  # Check if schedule_limit is greater than or equal to current date
                    timestamp__isnull=True
                )
                if user_schedule.count() == 1:
                    schedule = user_schedule.first()
                    print("WOI", schedule.id)
                    current_time = datetime.now()
                    schedule.timestamp = current_time
                    schedule.status = "present"
                    if(schedule.is_now_between_schedule()):
                        schedule.save()
                        messages.success(request, 'Absensi Berhasil cuk')

                return JsonResponse(data)

            else:  
                data = {
                    'status' : False,
                    'message' : 'Bukan Pengguna'
                }
                print(data)
                # auth.logout(request)
                return JsonResponse(data)
            
           
        else:
            data ={
                    'status' : False,
                    'message' : 'nim atau password Salah'
            }
            return JsonResponse(data)
    else:
        return render(request, 'loginform.html')

def logout_user(request):
    auth.logout(request)
    return redirect('beranda')


def absensi(request):
    if request.user.is_authenticated:
        return render(request, "absensi.html")
    return redirect('loginform')

def jadwalkuliah(request):
    if request.user.is_authenticated:

        return render(request, "jadwalkuliah.html")
    return redirect('loginform')

def jadwaltoday(request):
    if request.user.is_authenticated:
        user_data = request.session.get("user_data")
        current_date = date.today()
        user = User.objects.get(username=user_data['username'])
        user_schedule = Presence.objects.filter(
            user = user,
            schedule__date=current_date
        )
        return render(request, "jadwaltoday.html", {"user_schedule" : user_schedule} )
    return redirect('loginform')

def konfirmasi_hadir(request, presence_id):
    if request.user.is_authenticated and request.method == 'GET': 
        try:
            presence = Presence.objects.get(id=presence_id)
            current_time = datetime.now()
            presence.timestamp =  current_time
            presence.status =  "present"
            if(presence.is_now_between_schedule()):
                presence.save()
                messages.success(request, 'Absensi Berhasil')
            else: 
                messages.error(request, 'Absensi Gagal, Konfirmasi Di luar Waktu Absen')
            return redirect("jadwaltoday")
        except Exception as e:
            messages.error(request, f'Absensi Gagal, Error: {str(e)}')
            return redirect('jadwaltoday')


        