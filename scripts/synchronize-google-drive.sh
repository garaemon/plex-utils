#!/bin/bash
set -e

export PYTHONUNBUFFERED=x

rclone sync -P gdrive:Music/radio /mnt/external_hdd/GoogleDriveMusic/radio

python3 /home/ryohei/gprog/plex-utils/scripts/organize_music_files.py \
        /mnt/external_hdd/GoogleDriveMusic/radio/ /mnt/external_hdd/Music/radio/
