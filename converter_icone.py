from PIL import Image

imagem = Image.open("diarias.png")

imagem.save(
    "diarias.ico",
    format="ICO",
    sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]
)

print("Ícone convertido com sucesso!")