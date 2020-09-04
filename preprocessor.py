import cv2 as cv
import numpy as np

from contrast_stretcher import ContrastStretcher
from top_hat_filter import TopHatFilter
from otsu_thresholder import OtsuThresholder
from thresholder import Thresholder
from skimage.filters import frangi


class Preprocessor:
    FLUO_THRESHOLD = 129
    DIC_THRESHOLD = 5

    def __init__(self, image, mode):
        self.image = image
        self.mode = mode

    def preprocess(self):
        image = self.image
        kernel = np.ones((5, 5), np.uint8)
        if self.mode == 0:  # DIC
            image = frangi(image, sigmas=[15])
            image = ContrastStretcher(image).stretch()
            image = Thresholder(image, Preprocessor.DIC_THRESHOLD).threshold()
        if self.mode == 1:  # Fluo:
            image = Thresholder(image, Preprocessor.FLUO_THRESHOLD).threshold()
        else:       # PhC
            image = TopHatFilter(image).filter()
            image = OtsuThresholder(image).threshold()

        # Morphology
        image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
        image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
        return image
