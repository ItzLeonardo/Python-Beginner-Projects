from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
filtered_img = img.convert("L")
filtered_img.save("grey.png", 'png')