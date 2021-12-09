import os

lista_arquivos = os.listdir('D:\\')

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\pdf\\{arquivo}")
    if  ".docx" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\textos\\{arquivo}")
    if ".xlsx" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\excel\\{arquivo}")
    if ".csv" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\excel\\{arquivo}")
    if ".mp3" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\audio\\{arquivo}")
    if ".zip"  in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\zip\\{arquivo}")
    if ".mp3" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\audio\\{arquivo}")
    if ".mp4" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\audio\\{arquivo}")
    if ".exe" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\instaladores\\{arquivo}")
    if ".exe" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\instaladores\\{arquivo}")
    if ".png" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\imagem\\{arquivo}")
    if ".jpg" in arquivo:
        os.rename(f"D:\\{arquivo}", f"D:\\imagem\\{arquivo}")





