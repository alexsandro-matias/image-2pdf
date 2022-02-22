import os
from PIL import Image

def convert(path):
    imagem = Image.open(path)
    arquivo_pdf = imagem.convert('RGB')
    arquivo_pdf.save(path.replace(".png", ".pdf"))

diretorio = "C:\\Users\\almei\\Downloads\\github\\image-2pdf\\imagens"
arquivos = os.listdir(diretorio)

for f in arquivos:
    convert(os.path.join(diretorio, f))