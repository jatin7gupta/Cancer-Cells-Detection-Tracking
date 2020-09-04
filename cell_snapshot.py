import cv2 as cv
import numpy as np
from scipy.spatial.distance import euclidean
from math import inf


class CellSnapshot:
    def __init__(self, centroid, size, angle):
        # Shape
        self.centroid = centroid
        self.size = size
        self.angle = angle
        self.bounding_points = None
        # Tracking
        self.cell = None    # Reference to the cell
        self.prev_snapshot = None   # Prev snapshot (might be parent)
        self.next_snapshots = list()  # Next snapshots (if > 1, they are children)
        self.is_mitosis = False
        # Metrics
        self.speed = None
        self.total_distance = None
        self.net_distance = None
        self.confinement = None

    def get_bounding_points(self):
        if self.bounding_points is not None:
            return self.bounding_points

        self.bounding_points = np.intp(
            cv.boxPoints((self.centroid, self.size, self.angle))
        )
        return self.bounding_points

    def set_prev_snapshot(self, prev_snapshot):
        self.prev_snapshot = prev_snapshot

    def associate(self, cell):
        self.cell = cell

    def confirm_mitosis(self):
        self.is_mitosis = True

    def add_next_snapshot(self, snapshot):  # Also detect mitosis
        self.next_snapshots.append(snapshot)
        # Detect mitosis and mark
        next_snapshots_count = len(self.next_snapshots)
        if next_snapshots_count == 2:
            for snapshot in self.next_snapshots:
                snapshot.confirm_mitosis()
        elif next_snapshots_count > 2:
            snapshot.confirm_mitosis()

    def is_point_inside(self, point):
        return cv.pointPolygonTest(
            self.get_bounding_points(), point, False
        ) >= 0

    def update_cell_mileage(self):
        if self.get_speed() is None:
            return

        self.cell.update_mileage(self.get_speed())

    def get_speed_display(self):
        if self.get_speed() is None:
            return 'N/A'

        return f'{self.get_speed():.2f}'

    def get_speed(self):
        if self.speed is not None:
            return self.speed

        if self.prev_snapshot is None:
            return

        self.speed = (
            euclidean(self.centroid, self.prev_snapshot.centroid)
        )
        return self.speed

    def get_total_distance_display(self):
        if self.get_total_distance() is None:
            return 'N/A'

        return f'{self.get_total_distance():.2f}'

    def get_total_distance(self):
        if self.total_distance is not None:
            return self.total_distance

        if self.cell is None:
            return

        self.total_distance = self.cell.mileage
        return self.total_distance

    def get_net_distance_display(self):
        if self.get_net_distance() is None:
            return 'N/A'

        return f'{self.get_net_distance():.2f}'

    def get_net_distance(self):
        if self.net_distance is not None:
            return self.net_distance

        if self.cell is None:
            return

        self.net_distance = euclidean(self.centroid, self.cell.origin)
        return self.net_distance

    def get_confinement_display(self):
        if self.get_confinement() is None:
            return 'N/A'

        if self.get_confinement() == inf:
            return 'Infinity'

        return f'{self.get_confinement():.2f}'

    def get_confinement(self):
        if self.confinement is not None:
            return self.confinement

        if (self.get_total_distance() is None
                or self.get_net_distance() is None):
            return

        if self.get_net_distance() == 0:
            return inf

        self.confinement = self.get_total_distance() / self.get_net_distance()
        return self.confinement
