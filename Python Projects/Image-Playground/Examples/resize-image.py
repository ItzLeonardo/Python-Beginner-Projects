from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
resize = img.resize((300, 300))
resize.save("resize.png", 'png')