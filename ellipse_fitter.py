import cv2 as cv
import global_vars
import numpy as np

from cell_snapshot import CellSnapshot


class EllipseFitter:
    CANNY_THRESHOLD = 100
    MIN_CONTOUR_POINTS = 5

    def __init__(self, image, mode):
        self.image = image
        self.mode = mode

    def fit(self):
        # Canny
        threshold = EllipseFitter.CANNY_THRESHOLD
        edges = cv.Canny(self.image, threshold, threshold * 2)

        # Find Contour
        _, contours, _ = cv.findContours(
            edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        ellipses = list()
        for i, contour in enumerate(contours):
            if contour.shape[0] > EllipseFitter.MIN_CONTOUR_POINTS:
                ellipse = cv.fitEllipse(contour)
                if self.is_size_ok(ellipse):
                    ellipses.append(ellipse)

        return np.array([CellSnapshot(*ellipse) for ellipse in ellipses])

    def is_size_ok(self, ellipse):
        if self.mode != 0:
            return True

        width, height = ellipse[1]
        ratio = (width * height) / global_vars.image_area
        return 0.01 < ratio and ratio < 0.2
