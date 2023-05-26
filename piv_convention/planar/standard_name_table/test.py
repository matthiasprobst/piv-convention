import yaml


def test_read():
    with open('particle_image_velocimetry-v1.yaml', 'r') as f:
        _dict = {}
        for d in yaml.full_load_all(f):
            _dict.update(d)


if __name__ == '__main__':
    test_read()
