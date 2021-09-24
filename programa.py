# pip install Pillow

from PIL import Image

imagem = Image.open(r'image.png')
arquivo_pdf = image1.convert('RGB')
arquivo_pdf.save(r'doc.pdf')
