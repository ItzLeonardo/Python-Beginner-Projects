from PIL import Image, ImageFilter

img = Image.open("./sharpen.png")
box = (100, 100, 400, 400)
crop = img.crop(box)
crop.save("crop.png", 'png')
