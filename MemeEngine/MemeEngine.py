import random

from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    def __init__(self, output_directory):
        self.output_directory = output_directory

    def make_meme(self, img_path, body, author, req_width=500) -> str:
        img = Image.open(img_path)
        print(img.size)
        width, height = img.size
        scale = req_width/width
        height *= scale
        print(height)

        img = img.resize((int(req_width), int(height)), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./LilitaOne-Regular.ttf', size=20)
        # font = ImageFont.truetype('../_data/fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((10,30), f'{body} -\n{author}', font=font, fill='white')   #the location of the text needs to be randomly generated

        out_path = img.save(f'{self.output_directory}/{random.randint(0,100000)}.png')
        return out_path
