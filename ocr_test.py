from PIL import Image
import pytesseract
import shutil
import os


def ocr_test(images_dir):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    images = os.listdir(images_dir)
    if not os.path.exists('ImagenesFiltradas'):
        os.makedirs('ImagenesFiltradas')
    cont = 0
    keys = ['SISTEMAS','INGENIERO','ANALISTA', 'RPA','ETL','DATOS']
    for i in range(len(images)):
        image = Image.open(f'images/{images[i]}')
        texto_extraido = pytesseract.image_to_string(image)
        for palabra in keys:
            if palabra in texto_extraido:
                shutil.move(f'images/{images[i]}','ImagenesFiltradas/')  
                print(f"La palabra clave '{palabra}' se encontró en el texto.")
                cont +=1
    
    print('Aciertos: ', cont)


ocr_test('images')