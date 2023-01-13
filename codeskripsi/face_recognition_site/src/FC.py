import face_recognition
import cv2
import glob
import numpy as np

class FaceRecognitionMaulizar:
    def __init__(self):
        pass

    #Baca gambar pada setiap path 
    # *Note Gambar harus dalam .jpg
    def tampilkan_gambar(self, path):
        self.img = cv2.imread(path)
        cv2.imshow("hasil", self.img)
        cv2.waitKey(0)

    #load semua nama yang ada di .txt
    def load_name(self, path_name):
        self.name_container = []
        with open(path_name, 'r') as f:
            self.names =  f.readlines()
            for nama in self.names:
                self.name_container.append(nama.replace("\n", ""))
        return self.name_container

    #load nama file untuk setiap gambar yang ada di data poto (PATH_POTO)
    def load_img_path(self, path_poto):
        self.path_container = []
        for file in glob.glob(path_poto ):
            self.path_container.append(file)
        return self.path_container
            
    #untuk load gambar di database, dipangggil jika ada gambar baru di database
    def load_image(self, path_poto):
        self.img_paths = self.load_img_path(path_poto)
        self.data_container = []
        for img in self.img_paths:
            try:
                self.data_container.append(face_recognition.face_encodings(face_recognition.load_image_file(img))[0])
            except IndexError:
                print("tidak ada muka terdeteksi ..")
                quit()
        return self.data_container

    #digunakan untuk mengecek gambar apakah orang tersebut ada atau tidak di database
    #return "False, Unkown" jika tidak ada didatabase
    #return "True, Nama_orang" jika ada didatabase
    def cek_wajah(self, load_img, path_name, unknown_image): #unknown_image = path unknwon img
        self.names = self.load_name(path_name)
        self.unknown_image_encode = face_recognition.face_encodings(face_recognition.load_image_file(unknown_image))[0]
        self.results = face_recognition.compare_faces(load_img, self.unknown_image_encode)
        self.results_idx = np.argmax(self.results)

        if sum(self.results) !=0:
            return True, self.names[self.results_idx]
        else:
            return False, "Unkown"
