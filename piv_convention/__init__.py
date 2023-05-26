"""PIV convention for HDF5 files.

This repository currently contains the basic piv convention which is valid for planar (2D2C and 2D3C) PIV data.
"""

from .planar.convention import planar_convention

from .planar.layout import PIVLayout


def validate(target):
    """Validate the target file (HDF5 file instance or path) against the PIV layout."""
    PIVLayout.validate(target)
    return PIVLayout


__all__ = ['PIVLayout', ]

planar_convention.register()
