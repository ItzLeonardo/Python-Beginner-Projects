from PIL import Image, ImageFilter

img = Image.open("./fox.jpg")

img.thumbnail((500, 600))
img.save("thumbnail.jpg")
