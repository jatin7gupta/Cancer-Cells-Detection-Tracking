import numpy as np
import cv2 as cv


class TopHatFilter:
    def __init__(self, image, neighborhood_size=25, morph=cv.MORPH_OPEN):
        self.image = image
        self.neighborhood_size = neighborhood_size
        self.morph = morph

    def filter(self):
        kernel = np.ones(
            (self.neighborhood_size, self.neighborhood_size), np.uint8)
        background = cv.morphologyEx(self.image, self.morph, kernel)
        return cv.subtract(self.image, background)
