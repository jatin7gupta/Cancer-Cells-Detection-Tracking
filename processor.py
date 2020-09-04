import cv2 as cv
import math
import sys
import time
import global_vars

from boxes_drawer import BoxesDrawer
from cell import Cell
from cell_associator import CellAssociator
from directory_reader import DirectoryReader
from preprocessor import Preprocessor
from ellipse_fitter import EllipseFitter


class Processor:
    def __init__(self, file, mode, prev_snapshots):
        self.file = file
        self.mode = mode
        self.prev_snapshots = prev_snapshots
        self.curr_snapshots = None

    def process(self):
        # Read image
        image = cv.imread(self.file, cv.IMREAD_GRAYSCALE)

        # Save global information
        if global_vars.image_size is None:
            global_vars.image_size = image.shape[1::-1]
        if global_vars.image_diag is None:
            global_vars.image_diag = math.hypot(*global_vars.image_size)
        if global_vars.image_area is None:
            global_vars.image_area = (
                global_vars.image_size[0]
                * global_vars.image_size[1]
            )

        # Preprocess image
        preprocessed_image = Preprocessor(image, self.mode).preprocess()

        # Segment image
        self.curr_snapshots = EllipseFitter(
            preprocessed_image, self.mode
        ).fit()

        # Associate
        self.associate_cells()

        # Draw bounding box
        boxed_image = BoxesDrawer(self.curr_snapshots, image).draw()
        return boxed_image, self.curr_snapshots

    def associate_cells(self):
        if self.prev_snapshots is None:  # Initialize (Frame 0)
            for snapshot in self.curr_snapshots:
                new_id = len(global_vars.cells)  # ID of new cell
                cell = Cell(new_id, snapshot.centroid)  # New Cell
                global_vars.cells.append(cell)              # Add to DB

                # Associate snapshot with the new cell
                snapshot.associate(cell)
            return self.curr_snapshots
        else:
            # Association threshold
            if self.mode == 0:   # DIC
                threshold = 0.1
            elif self.mode == 1:   # Fluo
                threshold = 0.025
            else:  # PhC
                threshold = 0.01

            # Association happens here
            associator = CellAssociator(
                self.curr_snapshots, self.prev_snapshots, threshold
            )
            return associator.associate()
