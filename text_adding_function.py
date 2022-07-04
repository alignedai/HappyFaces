from PIL import Image, ImageDraw, ImageFont

def add_text(old_image, text, new_image):
    my_image = Image.open(old_image)
    image_editable = ImageDraw.Draw(my_image)
    myFont = ImageFont.truetype('DejaVuSans-Bold.ttf', 50) #or wherever the font file is
    W, H = my_image.size
    w, h = image_editable.textsize(text, font=myFont)
    image_editable.text(((W - w) / 2, ((H) * 8 / 9) - h / 2), text, fill="red", font=myFont)
    my_image.save(new_image)
    return my_image
