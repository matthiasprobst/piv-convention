import h5rdmtoolbox as h5tbx


def test_use():
    """test piv_convention"""
    assert 'planar_piv' not in h5tbx.conventions.registered_conventions.keys()
    # import piv_convention
    from piv_convention import planar_convention
    assert planar_convention.name in h5tbx.conventions.registered_conventions.keys()
