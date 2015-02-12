__author__ = 'Federico Tomassetti'

# Please refer to README.md in this directory

import os
from lands.world import *
from lands.draw import *


def main(blessed_images_dir, tests_data_dir):
    w = World.open_protobuf("%s/seed_28070.world" % tests_data_dir)
    draw_simple_elevation_on_file(w.elevation['data'], "%s/simple_elevation_28070.png" % blessed_images_dir, w.width, w.height, w.sea_level())
    draw_elevation_on_file(w, "%s/elevation_28070_shadow.png" % blessed_images_dir, shadow=True)
    draw_elevation_on_file(w, "%s/elevation_28070_no_shadow.png" % blessed_images_dir, shadow=False)
    draw_riversmap_on_file(w, "%s/riversmap_28070.png" % blessed_images_dir)
    draw_grayscale_heightmap_on_file(w, "%s/grayscale_heightmap_28070.png" % blessed_images_dir)
    draw_watermap_on_file(w, "%s/watermap_28070_th05.png" % blessed_images_dir, 0.5)


if __name__ == '__main__':
    blessed_images_dir = os.path.dirname(os.path.realpath(__file__))
    tests_data_dir = os.path.abspath(os.path.join(blessed_images_dir, '../data'))
    main(blessed_images_dir, tests_data_dir)