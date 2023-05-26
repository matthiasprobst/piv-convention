from typing import Tuple

from h5rdmtoolbox.conventions.standard_attribute import StandardAttribute


class FinalInterrogationWindow(StandardAttribute):
    """Units attribute"""

    name = 'final_window_size'

    def get(self) -> Tuple[int, int]:
        """Return the final interrogation window size. Expects datasets
        'x_pixel_coordinate' and 'y_pixel_coordinate'."""
        root = self.parent
        ix = root.find_one({'standard_name': 'x_pixel_coordinate'})
        fws_x = ix[1] - ix[0]
        iy = root.find_one({'standard_name': 'y_pixel_coordinate'})
        fws_y = iy[1] - iy[0]
        assert fws_x > 0
        assert fws_y > 0
        return int(fws_x), int(fws_y)

    def set(self, *args, **kwargs):
        """Set window size"""
        raise RuntimeError('Attribute "final_window_size" is read-only')
