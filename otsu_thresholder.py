import cv2 as cv


class OtsuThresholder:
    def __init__(self, image):
        self.image = image

    def threshold(self):
        _, result = cv.threshold(
            self.image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
        )

        return result
