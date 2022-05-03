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

        font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', size=20)

        x, y = 20, random.randint(0,int(0.8*height))

        tint_colour = (0,0,0)
        transparency = 0.50
        opacity = int(225 * transparency)
        img = img.convert('RGBA')

        overlay = Image.new('RGBA', img.size, tint_colour+(0,))
        drawOverlay = ImageDraw.Draw(overlay)
        drawOverlay.rectangle(((0,y), (req_width,y+50)), fill=tint_colour+(opacity,))
        
        drawOverlay.text((x,y), f'{body} -\n{author}', font=font, fill='white')
        img.convert('RGB')

        img = Image.alpha_composite(img, overlay)       
        out_path = f'{self.output_directory}/{random.randint(0,100000)}.png'
        img.save(out_path)
        return out_path
