import pathlib
import shutil

try:
    from h5rdmtoolbox.conventions.standard_name import StandardNameTable
except ImportError:
    raise ImportError('h5rdmtoolbox missing. you need to install it to check for standard name tables')
__this_dir__ = pathlib.Path(__file__).parent


def sort():
    """Sorts the standard name table"""

    shutil.copy(__this_dir__ / 'particle_image_velocimetry-v1.yaml',
                __this_dir__ / 'particle_image_velocimetry-v1.yaml.bak')
    snt_local = StandardNameTable.from_yaml(
        __this_dir__ / 'particle_image_velocimetry-v1.yaml.bak'
    )
    snt_local.to_yaml(__this_dir__ / 'particle_image_velocimetry-v1.yaml')  # automatically sorts
    return snt_local


README_HEADER = """# Planar PIV Standard Name Table

| Standard Name |     units     | Description |
|---------------|:-------------:|:------------|
"""


def update_readme():
    with open(__this_dir__ / 'README.md', 'w') as f:
        f.write(README_HEADER)
        for k, v in sort().table.items():
            f.write(f'| {k} | {v["canonical_units"]} | {v["description"]} |\n')


if __name__ == '__main__':
    # sort()
    update_readme()
