from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
rotate = img.rotate(180)
rotate.save("rotate.png", 'png')
