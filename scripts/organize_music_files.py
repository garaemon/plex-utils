#!/usr/bin/env python

import os
import sys
import shutil
from mutagen.easyid3 import EasyID3


def main(from_directory, to_directory):
    for root, _dirs, files in os.walk(from_directory):
        for f in files:
            from_path = os.path.join(root, f)
            if from_path.endswith('.mp3'):
                tags = EasyID3(from_path)
                if 'album' not in tags:
                    print('{} does not have album'.format(from_path))
                    continue
                album = tags['album']
                to_directory = os.path.join(to_directory, album)
                to_path = os.path.join(to_directory, f)
                if not os.path.exists(to_directory):
                    print('Creating Album directory'.format(to_directory))
                    os.makedirs(to_directory)
                if not os.path.exists(to_path):
                    print('Copying {} to {}'.format(from_path, to_path))
                    shutil.copy(from_path, to_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
