"""Define MemeEngine class."""

import random
import textwrap
import math

from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """MemeEngine class."""

    def __init__(self, output_directory):
        """
        Instanciates the MemeEngine object.

        @param output_directory (string): intended output directory for
        the generated memes.
        """
        self.output_directory = output_directory

    def make_meme(self, img_path, body, author, req_width=500) -> str:
        """
        Create the meme.

        @param: img_path (string): path to image to use as base for meme.
        @param: body (string): body to use as the body text of the meme.
        @param: athor (string): author to use as the author text of the meme.
        @param: req_width (int, optional): Width for generated meme.
        Defaults to 500px.

        Returns: file path to generated meme.
        """
        img = Image.open(img_path)
        width, height = img.size
        scale = req_width/width
        height *= scale

        img = img.resize((int(req_width), int(height)), Image.NEAREST)

        font = ImageFont.truetype(
            './_data/fonts/LilitaOne-Regular.ttf', size=20)

        x, y = 20, random.randint(0, int(0.6*height))

        tint_colour = (0, 0, 0)
        transparency = 0.50
        opacity = int(225 * transparency)
        img = img.convert('RGBA')

        wrapper = textwrap.TextWrapper(width=50)
        wrapped_body = wrapper.fill(text=body)
        wrapped_author = wrapper.fill(text=author)

        overlay_height = (math.ceil(len(wrapped_body)/50)
                          + math.ceil(len(wrapped_author)/50) + 1)
        overlay = Image.new('RGBA', img.size, tint_colour+(0,))
        drawOverlay = ImageDraw.Draw(overlay)
        drawOverlay.rectangle(((0, y), (req_width, y + overlay_height*25)),
                              fill=tint_colour + (opacity, ))
        drawOverlay.text((x, y), f'{wrapped_body}\n\n-{wrapped_author}',
                         font=font, fill='white')
        img.convert('RGB')

        img = Image.alpha_composite(img, overlay)
        out_path = f'{self.output_directory}/{random.randint(0,100000)}.png'
        img.save(out_path)
        return out_path
