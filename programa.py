# pip install Pillow

from PIL import Image

image1 = Image.open(r'image.png')
im1 = image1.convert('RGB')
im1.save(r'doc.pdf')