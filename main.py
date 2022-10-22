# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image, ImageDraw, ImageFont

FILE_1 = '1.jpg'
FILE_2 = '2.png'
FONT_FAMILY = 'Roboto.ttf'
COLOR = (255, 0, 0, 100)
OFFSET = 5


def add_watermark(file, text):
    image = Image.open(file)
    type_image = 'RGB' if image.format == 'JPEG' else 'RGBA'
    image = image.convert('RGBA')
    image_watermark = Image.new('RGBA', image.size)
    draw = ImageDraw.Draw(image_watermark)
    width, height = image.size
    font = ImageFont.truetype(FONT_FAMILY, int(height / 10))

    text_width, text_height = draw.textsize(text, font)
    text_x = width - text_width - OFFSET
    text_y = height - text_height - OFFSET

    draw.text((text_x, text_y), text, COLOR, font)
    result = Image.alpha_composite(image, image_watermark)
    result.convert(type_image).save('watermark_' + file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_watermark(FILE_1, 'My watermark')
    add_watermark(FILE_2, 'My watermark')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
