from src.FC import FaceRecognitionMaulizar
from src import config

face_recognition = FaceRecognitionMaulizar()

#load image dari database
image = face_recognition.load_image(config.PATH_POTO)

#check wajah
result = face_recognition.cek_wajah(image, config.PATH_NAME, config.PATH_TEST)

#tampilkan gambar
#face_recognition.tampilkan_gambar(config.PATH_TEST)

#cetak hasil
print(result)