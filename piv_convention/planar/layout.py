"""Particle Image Velocimetry conventions

It holds
 - PIVLayout: The definition on how a PIV file shall look like: groups, datasets and attributes
 - PIVStandardNameTable: Standard name table for PIV in air

"""

import json
from h5rdmtoolbox._config import ureg
from h5rdmtoolbox.conventions.layout import Layout
from h5rdmtoolbox.conventions.layout.tbx import IsValidContact
from h5rdmtoolbox.conventions.layout.validators import In
from h5rdmtoolbox.conventions.layout.validators import Validator, ValidString, Regex
from h5rdmtoolbox.conventions.standard_name import is_valid_unit
from typing import Dict


class IsValidUnit(Validator):
    """Valid units. Does this by checking if the unit can be understood by package 'ureg'"""

    def __init__(self, optional: bool = False):
        super().__init__(None, optional=optional)

    def __set_message__(self, target: str, success: bool):
        if success:
            self._message = f'"{target}" is a unit'
        else:
            self._message = f'"{target}" is not a unit'

    def validate(self, value):
        if self.is_optional:
            return True
        return is_valid_unit(value)


class IsValidStandardName(Regex):
    """Validates a standard name by checking the pattern"""

    def __init__(self, optional: bool = False):
        super().__init__(r'^[a-z][a-z0-9_]*$', optional=optional)

    def __str__(self):
        return "is valid standard name pattern"


class IsValidVersionString(Validator):
    """Validates a version string by using the class packaging.version.Version"""

    def __init__(self, optional: bool = False):
        super().__init__(None, optional=optional)

    def __str__(self):
        return "is valid version string"

    def validate(self, value):
        from packaging.version import Version, InvalidVersion
        try:
            Version(value)
            return True
        except InvalidVersion:
            return False


def _is_subset(dict1, dict2):
    """check if dict1 is a subset of dict2"""
    for k, v in dict1.items():
        if k not in dict2 or dict2[k] != v:
            return False
    return True


class ValidFlagMeanings(Validator):

    def __init__(self, valid_flags: Dict, optional: bool = False):
        super().__init__(valid_flags, optional=optional)

    def validate(self, value: Dict) -> bool:
        """check if value is a subset of the reference flag dict"""
        if isinstance(value, str):
            value = {int(k): v for k, v in json.loads(value).items()}
        return _is_subset(value, self.reference)


class IsSIUnit(Validator):

    def __init__(self, unit, optional: bool = False):
        super().__init__(reference=unit, optional=optional)

    def __str__(self):
        return f"Is SI unit {self.reference}"

    def __set_message__(self, target: str, success: bool):
        if success:
            self._message = f'"{target}" is SI-unit {self.reference}'
        else:
            self._message = f'{target} is not SI-unit {self.reference}'

    def validate(self, value) -> bool:
        if self.is_optional:
            return True
        is_unit = is_valid_unit(value)
        if not is_unit:
            return False
        return ureg.Unit(value).is_compatible_with(self.reference)


def create_piv_layout():
    """Creates the layout for a PIV file"""

    lay = Layout()
    lay['/'].attrs['title'] = ValidString()
    lay['*'].specify_dataset(name=..., opt=True).specify_attrs(dict(units=IsValidUnit(),
                                                                    standard_name=IsValidStandardName()))

    lay['/'].attrs['piv_medium'] = In('air', 'water')
    # A contact may be an an email or an ORCID, or multiple. Best is ORCID.
    lay['/'].attrs['contact'] = IsValidContact()

    # There must be datasets with the following standard names:
    any_ds = lay['/'].specify_dataset(name=..., opt=True)
    # any_ds.specify_attrs(dict(standard_name=..., units=...))
    any_ds.specify_attrs(dict(standard_name='x_velocity', units=IsSIUnit('m/s')), count=1)
    any_ds.specify_attrs(dict(standard_name='y_velocity', units=IsSIUnit('m/s')), count=1)
    any_ds.specify_attrs(dict(standard_name='x_coordinate', units=IsSIUnit('m')), count=1)
    any_ds.specify_attrs(dict(standard_name='y_coordinate', units=IsSIUnit('m')), count=1)
    any_ds.specify_attrs(dict(standard_name='x_pixel_coordinate', units=IsSIUnit('pixel')), count=1)
    any_ds.specify_attrs(dict(standard_name='y_pixel_coordinate', units=IsSIUnit('pixel')), count=1)
    any_ds.specify_attrs(dict(standard_name='signal_to_noise', units=In('', ' ')), count=1)
    any_ds.specify_attrs(dict(standard_name='time', units=IsSIUnit('s')), count=1)
    FLAGS = {0: 'INACTIVE',
             1: 'ACTIVE',
             2: 'MASKED',
             4: 'NORESULT',
             8: 'DISABLED',
             16: 'FILTERED',
             32: 'INTERPOLATED',
             64: 'REPLACED',
             128: 'MANUALEDIT'}
    any_ds.specify_attrs(dict(standard_name='piv_flags',
                              units=In('', ' '),
                              flag_meaning=ValidFlagMeanings(FLAGS)), count=1)
    return lay


PIVLayout = create_piv_layout()
