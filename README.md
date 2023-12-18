# Pengenal-Citra-Nomor-Kendaraan
Project Pengenal Citra Nomor Kendaraan sedang dalam progres, disini saya mengumpulkan 712 citra kendaran yang terbagi menjadi 4 cluster (K1, K2, K3, K4).
K1: Plat Hitam Motor
K2: Plat Putih Motor
K3: Plat Hitam Mobil
K4: Plat Putih Mobil

Pemrosesan Gambar dimulai dari mengumpulkan data dan memberi label pada gambar untuk mendeteksi objek Plat Nomor atau Plat menggunakan Alat Anotasi Gambar yang merupakan perangkat lunak sumber terbuka yang dikembangkan dengan python GUI (pyQT).

Kemudian setelah dilabeli pada gambar akan dilakukan preprocessing data, membangun dan melatih model deteksi objek dengan CNN  menggunakan (InceptionResnet V2) di TensorFlow 2. Hingga model dilatih dengan capaian RMSE terbaik.

Setelah selesai dengan model Deteksi Objek, kemudian dengan menggunakan model ini kita akan memotong gambar yang berisi pelat nomor yang juga disebut Region of Interest (ROI), dan meneruskan ROI ke API Pengenalan Optical Character of the Tesseract dengan Python (Pytesseract). Dalam model ini,akan menggabungkan semuanya dan membangun model Pipeline CNN.

Pada modul terakhir, kita akan belajar membuat proyek aplikasi web menggunakan FLASK Python.
Arsitektur website menggunakan HTML, Bootstrap. Dan Aplikasi telah siap.