"""IEEE UMich Card Reader Development Configuration."""

# Written by Shuta Suzuki (shutas@umich.edu)

import os

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'insta485.sqlite3'
)
