import enum

from h5rdmtoolbox.conventions.standard_attribute import StandardAttribute


class PivMedium(StandardAttribute):
    name = 'piv_medium'


class PIVSeedingMaterials(enum.Enum):
    # Taken from "Particle Image Velocimetry - A Practical Guide" by Raffel et al.
    # Liquids:
    DEHS = 1  # 'Di-ethyl-hexyl-sebacate'  # 0.5-1.5 um
    DIETHYLHEXYLSEBACATE = 1  # DiEthylHexylSebacate
    HELIUMFILLEDSOAPBUBBLES = 2  # 'Helium-filled soap bubbles'  # 200-3000 um
    GLYCERINEWATERMIXTURE = 3  # 'Glycerine-water-mixture'  # 0.5-2.0 um
    # Solids:
    SMOKE = 4  # 'Smoke'  # < 1
    DIOTYLPHATHALATE = 5  # 'Diotylphathalate'  # 1-10 um
    GLASSMICROBALLOONS = 6  # 'Glass micro balloons'  # 30-100 um
    GLASSMICROSPHERES = 7  # 'Glass micro spheres'  # 0.2-3 um
    TITANIA = 8  # 'Titania'  # 0.1-5 um  (TiO2)
    TIO2 = 8
    ALUMINA = 9  # 'Alumina'  # 0.2-5 um  (Al2O3)
    Al2O3 = 9
    POLYSTYRENE = 10  # 'Polystyrene'  # 0.5-10 um


class PIVSeedingMaterial(StandardAttribute):
    name = 'piv_seeding_material'

    def set(self, value: str):
        """Set the seeding material"""
        if not isinstance(value, str):
            raise TypeError(f'Expected string, got {type(value)}')
        try:
            PIVSeedingMaterials[value.upper()]
        except KeyError:
            raise ValueError(f'Unknown seeding material {value}')
        self._parent.attrs[self.name] = value
