from . driver_base import DriverBase
import os
import sys
from .. import log

try:
    import PIL
    from PIL import Image, ImageDraw
except:
    Image, ImageDraw = None, None


class ImageSequence(DriverBase):

    def __init__(self, num=0, width=0, height=0, pixelSize=10):
        """delay: time to wait in milliseconds to simulate actual hardware interface time"""
        if not Image:
            error = "Please install Python Imaging Library: pip install pillow"
            log.error(error)
            raise ImportError(error)

        super().__init__(num, width, height)
        self._pixelSize = pixelSize
        self._images = []

        if self.width == 0 and self.height == 0:
            self.width = self.numLEDs
            self.height = 1

    # Push new data to strand
    def _send_packet(self):
        # TODO: This is all done on the I/O thread.  Some of this could be done
        # on the compute thread...
        map = self.matrix_map
        size = self._pixelSize
        img = Image.new("RGB", (self.width * size, self.height * size), None)
        draw = ImageDraw.Draw(img)
        for x in range(self.width):
            for y in range(self.height):
                if map:
                    i = map[y][x]
                else:
                    i = x
                rgb = self._colors[i + self._pos]
                # TODO: is it an issue that colors now are floats?
                draw.rectangle([x * size, y * size, x * size +
                                size - 1, y * size + size - 1], rgb, rgb)

        self._images.append(img)

    # use ImageMagick to combine and make the gif
    # convert -delay 25 -loop 0 *.png 0.gif
    def writeSequence(self, output, clear=True):
        count = 0
        for img in self._images:
            file = output + "/" + ("%04d" % count) + ".png"
            log.info("Writing: %s", file)
            img.save(file)
            count += 1

        if clear:
            self._images = []


# This is DEPRECATED.
DriverImageSequence = ImageSequence
