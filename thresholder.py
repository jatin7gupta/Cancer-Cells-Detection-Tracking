import cv2 as cv


class Thresholder:
    def __init__(self, image, value):
        self.image = image
        self.value = value

    def threshold(self):
        _, result = cv.threshold(self.image, self.value, 255, cv.THRESH_BINARY)

        return result
