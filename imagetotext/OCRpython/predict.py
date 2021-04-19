#import tesserocr
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ocr:
    def __init__(self, filename):
        self.filename = filename



    def getPrediction(self):
        image = Image.open(self.filename)
        lines = pytesseract.image_to_string(image)  # print ocr text from image
        #for line in lines.split("\r"):
         #   print(line)
        return lines


