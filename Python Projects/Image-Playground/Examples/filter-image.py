from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", 'png')