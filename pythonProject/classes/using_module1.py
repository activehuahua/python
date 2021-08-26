from PIL import Image

im = Image.open('test.png')
print(im.format, im.size, im.mode)

if im.mode != "RGB":
    im = im.convert("RGB")

im.thumbnail((200, .100))
im.save('thumb.jpg', 'JPEG')
