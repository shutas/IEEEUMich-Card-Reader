"""IEEE UMich Card Reader Configuration."""

# Written by Shuta Suzuki (shutas@umich.edu)

import os

# Email Address of Sender
SENDER_EMAIL = "ieee.umich.donotreply@gmail.com"

# Destination Email Address
DESTINATION_EMAIL = "IEEE.VPComm@umich.edu"

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'insta485.sqlite3'
)
