# AYIIIIIIII
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import face_recognition
import io, base64
import os
from PIL import Image
from django.http import JsonResponse
# from PIL import Image
# from base64 import decodestring
# from django.core.files.base import ContentFile
# Create your views here.

def beranda(request):
      
    # render function takes argument  - request
    # and return HTML as response
    print("tess")
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        print("success")
        return render(request, "home.html")
    else:
        print("failed")
        return redirect('loginform')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        camera_data = request.POST['camera_data']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #simpan gambar dari camera ke server
            img = Image.open(io.BytesIO(base64.decodebytes(bytes(camera_data.split("data:image/jpeg;base64,")[-1], "utf-8"))))
            img.save(os.path.abspath(f'codeskripsi/face_recog/image_temp/{username}.jpeg'))

            # load gambar yang dari server ke ml
            known_image_dir = f'codeskripsi/face_recog/user_images/{username}.jpeg'
            unknown_image_dir = f'codeskripsi/face_recog/image_temp/{username}.jpeg'
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
                    'message' : 'Username atau password Salah'
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
        return render(request, "jadwaltoday.html")
    return redirect('loginform')