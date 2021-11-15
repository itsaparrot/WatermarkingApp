import tkinter

from PIL import Image
from tkinter import filedialog

CANVAS_BACKGROUND = "#f7f5dd"


def upload_image():
    image_file = filedialog.askopenfilename(filetypes=[('Image Files', '*jpeg *jpg *png')])
    # opens file, then saves as png
    im1 = Image.open(image_file)
    im1.save('img/new_image.png')
    image_file = 'img/new_image.png'
    # updates canvas image with uploaded png
    active_img.config(file=image_file)


def upload_watermark():
    watermark = filedialog.askopenfilename(filetypes=[('Image Files', '*jpeg *jpg *png')])
    im1 = Image.open('img/new_image.png')
    width, height = im1.size
    # finds size of image to make the watermark's size relative to it
    size = (width * 0.3, height * .3)
    image_watermark = Image.open(watermark)
    cropped_image = image_watermark.copy()
    cropped_image.thumbnail(size)
    # makes the image transparent
    cropped_image.putalpha(135)

    # coordinates for placing watermark image, placing it on the right side of the image
    x = round(width / 2) + (width * 0.15)
    y = round(height / 2)
    # paste watermark onto original image, passing the same image as third parameter keeps it transparent
    im1.paste(cropped_image, (round(x), round(y)), cropped_image)
    im1.save('img/watermarked_image.png')
    watermarked_image = 'img/watermarked_image.png'
    active_img.config(file=watermarked_image)


window = tkinter.Tk()
window.title("Watermark App")
window.config(padx=50, pady=50, bg=CANVAS_BACKGROUND)

canvas = tkinter.Canvas(width=600, height=400, bg=CANVAS_BACKGROUND, highlightthickness=0)
active_img = tkinter.PhotoImage(file="")
canvas.create_image(300, 200, image=active_img)
canvas.grid(column=1, row=1)

# buttons, open first image, open image to use as watermark, save new image
button = tkinter.Button(text='Open Image', command=upload_image)
button.grid(column=0, row=2)
button = tkinter.Button(text='Place Watermark', command=upload_watermark)
button.grid(column=2, row=2)

window.mainloop()
