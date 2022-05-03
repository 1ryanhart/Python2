import random

from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    def __init__(self, output_directory):
        self.output_directory = output_directory

    def make_meme(self, img_path, body, author, req_width=500) -> str:
        img = Image.open(img_path)
        width, height = img.size
        scale = req_width/width
        height *= scale

        img = img.resize((int(req_width), int(height)), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', size=20)

        x, y = random.randint(0,int(0.5*req_width)), random.randint(0,int(0.8*height))
        draw.text((x,y), f'{body} -\n{author}', font=font, fill='white')

        out_path = f'{self.output_directory}/{random.randint(0,100000)}.png'
        img.save(out_path)
        return out_path
