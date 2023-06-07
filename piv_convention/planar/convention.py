from h5rdmtoolbox.conventions import Convention
from h5rdmtoolbox.conventions.contact import ContactAttribute
from h5rdmtoolbox.conventions.title import TitleAttribute

from .general_attributes import PivMedium, PIVSeedingMaterial
from .piv_settings import FinalInterrogationWindow

planar_convention = Convention('planar_piv')

planar_convention['__init__'].add(attr_cls=FinalInterrogationWindow,
                        add_to_method=False)

planar_convention['__init__'].add(attr_cls=PivMedium,
                        add_to_method=True,
                        optional=True,
                        position=dict(before='layout'))

planar_convention['__init__'].add(attr_cls=PIVSeedingMaterial,
                        add_to_method=True,
                        optional=True,
                        position=dict(before='layout'))

planar_convention['__init__'].add(attr_cls=ContactAttribute,
                        add_to_method=True,
                        optional=True,
                        position=dict(before='layout'))

planar_convention['__init__'].add(attr_cls=TitleAttribute,
                        add_to_method=True,
                        optional=True,
                        position=dict(before='layout'))
