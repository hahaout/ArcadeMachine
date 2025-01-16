# This file is copied from https://www.pygame.org/wiki/Spritesheet

# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame


class Spritesheet(object):
    """TODO: placeholder."""

    def __init__(self, filename):
        """
        Initializes the Spritesheet object by loading the sprite sheet image.

        :param filename: The path to the sprite sheet image file.
        :raises SystemExit: If the sprite sheet image cannot be loaded.
        """
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print("Unable to load Spritesheet image:", filename)
            print("Unable to load Spritesheet image:", filename)
            raise SystemExit(message)

    def image_at(self, rectangle, colorkey=None):
        """
        Loads a specific image from the sprite sheet defined by a rectangle.

        :param rectangle: A tuple (x, y, width, height) that defines the area of the sprite to extract.
        :param colorkey: An optional color key for transparency. If set to -1, the top-left pixel will be used as the transparent color.
        :return: A pygame.Surface object containing the extracted sprite.
        """
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """
        Loads multiple images from the sprite sheet, each defined by a rectangle.

        :param rects: A list of tuples, where each tuple (x, y, width, height) defines an area of the sprite sheet.
        :param colorkey: An optional color key for transparency. If set to -1, the top-left pixel of each image will be used as the transparent color.
        :return: A list of pygame.Surface objects, each containing an extracted sprite.
        """
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        """
        Loads a strip of images from the sprite sheet.

        :param rect: A tuple (x, y, width, height) that defines the first sprite in the strip.
        :param image_count: The number of images in the strip.
        :param colorkey: An optional color key for transparency. If set to -1, the top-left pixel of each image will be used as the transparent color.
        :return: A list of pygame.Surface objects, each containing an extracted sprite from the strip.
        """
        tups = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        tups = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        return self.images_at(tups, colorkey)
