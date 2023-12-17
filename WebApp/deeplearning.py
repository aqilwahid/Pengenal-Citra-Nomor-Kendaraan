# Make Predictions
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import pytesseract as pt

model = tf.keras.models.load_model(
    "D:/UTY/Semester 7/Pengembangan Aplikasi AI/Pengenal-Citra-Nomor-Kendaraan/WebApp/static/models/object_detection.h5"
)


def object_detection(path, filename):
    # Read Image
    image = load_img(path)  # PIL object
    image = np.array(image, dtype=np.uint8)  # 8 bit array (0,255)
    image1 = load_img(path, target_size=(224, 224))
    # Data preprocessing
    image_arr_224 = (
        img_to_array(image1) / 255.0
    )  # Convert into array and get the normalized output
    h, w, d = image.shape  # size of the original image
    # Image Rotation
    rotation_matrix = cv2.getRotationMatrix2D(
        (w / 2, h / 2), -90, 1
    )  # Mendapatkan matriks rotasi
    image = cv2.warpAffine(
        image, rotation_matrix, (w, h)
    )  # Melakukan rotasi pada gambar
    # make predictions
    test_arr = image_arr_224.reshape(1, 224, 224, 3)
    coords = model.predict(test_arr)
    # Denormalize the values
    denorm = np.array([w, w, h, h])
    coords = coords * denorm
    coords = coords.astype(np.int32)  # Membulatkan
    # draw bounding on top the image
    xmin, xmax, ymin, ymax = coords[0]
    pt1 = (xmin, ymin)
    pt2 = (xmax, ymax)
    print(pt1, pt2)
    cv2.rectangle(image, pt1, pt2, (0, 255, 0), 30)
    # conver into bgr
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite("D:\UTY\Semester 7\Pengembangan Aplikasi AI\Pengenal-Citra-Nomor-Kendaraan\WebApp\static\predict{}".format(filename), image_bgr)
    return coords


def OCR(path, filename):
    pt.pytesseract.tesseract_cmd = (
        r"C:/Users/Aqil Wahid/AppData/Local/Tesseract-OCR/tesseract.exe"
    )
    image_to_string = pt.pytesseract.tesseract_cmd
    img = np.array(load_img(path))
    cods = object_detection(path, filename)
    xmin, xmax, ymin, ymax = cods[0]
    # size of the original image
    h, w, d = img.shape
    # Image Rotation
    rotation_matrix = cv2.getRotationMatrix2D(
        (w / 2, h / 2), -90, 1
    )  # Mendapatkan matriks rotasi
    img = cv2.warpAffine(img, rotation_matrix, (w, h))  # Melakukan rotasi pada gambar
    # Region of Interest
    roi = img[ymin:ymax, xmin:xmax]
    roi_bgr = cv2.cvtColor(roi, cv2.COLOR_RGB2BGR)
    cv2.imwrite("D:\UTY\Semester 7\Pengembangan Aplikasi AI\Pengenal-Citra-Nomor-Kendaraan\WebApp\static\roi{}".format(filename), roi_bgr)
    # extract text from image
    text = pt.image_to_string(roi)
    print("Plat Nomor:", text)
    return text
