# PIV Convention

Contains the `standard attbutes` and the `layout` specification. Both together assure either during or after the file
creation that the PIV file is complete and valid.

## Description

The "PIV convention" defines which attributes needs to be provided with a PIV file in order to consider it a complete
PIV file. Also, the values of these attributes are specified, e.g. that a contact person must not be a name but an
ORCID.

This convention can be used in two ways:

1. During data creation: The conventions must be enabled (`h5tbx.use('piv_convention')`)
2. After file creation/for existing files: The layout validation is performed by the `h5RDMtoolbox`
   package: `PIVLayout.validate_layout(<piv_hdf_filename>)`

### What is specified by the convention?

#### Flags:

### Standard name tables
- [planar](piv_convention/planar/standard_name_table/README.md)

### Available conventions

- `planar_piv`: The convention for planar PIV data (2D2C and 2D3C)

## Installation

```bash
pip install piv_convention
```

## Example

```python
import h5rdmtoolbox as h5tbx
import numpy as np

import piv_convention as pc

# enable the convention for the current session,
# to make sure that all (meta) data is written correctly
h5tbx.use('planar_piv')

with h5tbx.File('piv_file.hdf', 'w') as h5:
   h5.contact = '0000-0000-0000-0000'
   h5.create_dataset('u',
                     data=np.random.random((10, 20)),
                     units='mm/s', standard_name='velocity')
   # more data needed for a complete PIV file ...
   # ... for the sake of simplicity, we skip this here

# Perform the layout validation:
pc.validate('piv_file.hdf')
```

## Dependencies

The package highly depends on the HDF5 research management toolbox
`h5RDMtoolbox`